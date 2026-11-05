/*
 * Fries machine — CONTROL-LOGIC SIMULATION ONLY, version1.
 * Mega2560 / AVR Boards1.8.8 / hd44780 by Bill Perry1.3.2.
 * Existing wiring: buttons22/23/24 toGND; indexNO26/28/30, COMcommonGND,
 * NCempty; LCD GND/5V/SDA20/SCL21 at0x27. USB power only.
 *
 * Do not connect motors, driver inputs, a relay, heater or external supply.
 * There are NO actuator output pins or commands in this sketch/core.
 * Hand-operate the selected index to simulate a response, then watch5s
 * warm-up and10s cooking countdowns. These are NOT actual cooking settings.
 * Stop at SIM TIMERS DONE / Basket: pending, never claim a complete machine.
 * r (serial) or the Mega RESET button resets this bench simulation.
 */
#include <Arduino.h>
#include <Wire.h>
#include <stdio.h>
#include <string.h>
#include <hd44780.h>
#include <hd44780ioClass/hd44780_I2Cexp.h>
#include "ButtonInput.h"
#include "CycleLogic.h"

#if !defined(ARDUINO_AVR_MEGA2560)
#error "Use arduino:avr:mega:cpu=atmega2560"
#endif

constexpr uint8_t kInputCount = 6;
constexpr uint8_t kInputPins[kInputCount] = {22, 23, 24, 26, 28, 30};
constexpr uint8_t kLcdAddress = 0x27;
constexpr uint8_t kLcdColumns = 16;
constexpr uint8_t kLcdRows = 2;
constexpr uint32_t kWireTimeoutUs = 25000UL;
constexpr uint32_t kStatusIntervalMs = 2000UL;
constexpr uint32_t kDisplayIntervalMs = 100UL;
// Short BENCH timings. Machine proposal300s/600s must be implemented and
// thermally validated separately; do not use this sketch to run a fryer.
constexpr CycleTiming kSimulationTiming = {15000UL, 5000UL, 10000UL};
static_assert(SDA == 20 && SCL == 21, "LCD uses Mega SDA20/SCL21");
static_assert(kInputPins[3] == 26 && kInputPins[4] == 28 && kInputPins[5] == 30,
              "Match indexNO26/28/30 wiring");

hd44780_I2Cexp lcd(kLcdAddress);
ButtonInput inputs[kInputCount];
CycleLogic cycle(kSimulationTiming);
bool lcdReady = false;
uint32_t lastStatusMs = 0;
uint32_t lastDisplayMs = 0;
// Cache rows to avoid unnecessary I2C writes and display flicker.
char displayedRows[2][17] = {{0}, {0}};

void displayFault(const __FlashStringHelper* stage, int status) {
  lcdReady = false;  // Stop further display writes; retain input serial logs.
  Serial.print(F("CYCLE_SIM_V1 LCD_ERROR stage="));
  Serial.print(stage);
  Serial.print(F(" status="));
  Serial.println(status);
  Serial.println(F("Power off before checking LCD wiring. Inputs still log."));
}

bool writeLcdLine(uint8_t row, const char* text) {
  if (!lcdReady) {
    return false;
  }
  // Always write exactly one 16-character row, padding old text with spaces.
  char padded[kLcdColumns + 1];
  memset(padded, ' ', kLcdColumns);
  size_t length = strlen(text);
  if (length > kLcdColumns) {
    length = kLcdColumns;
  }
  memcpy(padded, text, length);
  padded[kLcdColumns] = '\0';

  const int status = lcd.setCursor(0, row);
  if (status != 0) {
    displayFault(F("cursor"), status);
    return false;
  }
  if (lcd.print(padded) != kLcdColumns) {
    displayFault(F("write"), -1);
    return false;
  }
  if (Wire.getWireTimeoutFlag()) {
    displayFault(F("timeout"), -2);
    return false;
  }
  return true;
}

const __FlashStringHelper* phaseName(CyclePhase phase) {
  switch (phase) {
    case CyclePhase::Idle: return F("IDLE");
    case CyclePhase::WaitIndex: return F("WAIT_INDEX");
    case CyclePhase::Warmup: return F("SIM_WARMUP");
    case CyclePhase::Cooking: return F("SIM_COOK");
    case CyclePhase::TimersDone: return F("TIMERS_DONE_BASKET_PENDING");
    case CyclePhase::Fault: return F("FAULT");
  }
  return F("INVALID");
}

void printStatus(uint32_t now) {
  Serial.print(F("CYCLE_SIM_V1 STATUS phase="));
  Serial.print(phaseName(cycle.phase()));
  Serial.print(F(" flavor="));
  Serial.print(cycle.flavor());
  Serial.print(F(" seconds="));
  Serial.print(cycle.secondsLeft(now));
  Serial.print(F(" raw="));
  for (uint8_t i = 0; i < kInputCount; ++i) Serial.print(digitalRead(kInputPins[i]));
  Serial.print(F(" lcd="));
  Serial.println(lcdReady ? F("OK") : F("FAULT"));
}

void drawSimulation(uint32_t now) {
  char rows[2][17] = {{0}, {0}};
  switch (cycle.phase()) {
    case CyclePhase::Idle:
      strcpy(rows[0], "SIMULATION ONLY");
      strcpy(rows[1], "Select flavor");
      break;
    case CyclePhase::WaitIndex:
      strcpy(rows[0], cycle.indexReleased() ? "SIM PRESS INDEX" : "SIM RELEASE IDX");
      snprintf(rows[1], sizeof(rows[1]), "Flavor %u %2lus", unsigned(cycle.flavor()),
               static_cast<unsigned long>(cycle.secondsLeft(now)));
      break;
    case CyclePhase::Warmup:
    case CyclePhase::Cooking:
      strcpy(rows[0], cycle.phase() == CyclePhase::Warmup ? "SIM WARMUP" : "SIM COOK");
      snprintf(rows[1], sizeof(rows[1]), "Flavor %u %2lus", unsigned(cycle.flavor()),
               static_cast<unsigned long>(cycle.secondsLeft(now)));
      break;
    case CyclePhase::TimersDone:
      strcpy(rows[0], "SIM TIMERS DONE");
      strcpy(rows[1], "Basket: pending");
      break;
    case CyclePhase::Fault:
      strcpy(rows[0], "SIM FAULT");
      strcpy(rows[1], cycle.fault() == CycleFault::IndexTimeout
                           ? "INDEX TIMEOUT" : "CONFIG INVALID");
      break;
  }
  for (uint8_t row = 0; row < 2; ++row) {
    if (strcmp(displayedRows[row], rows[row]) != 0 && writeLcdLine(row, rows[row])) {
      strcpy(displayedRows[row], rows[row]);
    }
  }
}

void setup() {
  digitalWrite(LED_BUILTIN, LOW);
  pinMode(LED_BUILTIN, OUTPUT);  // Only onboard LED; no actuator output setup.
  Serial.begin(115200);
  Serial.println(F("CYCLE_SIM_V1 boot: SIMULATION ONLY, NO ACTUATOR OUTPUTS"));
  for (uint8_t i = 0; i < kInputCount; ++i) {
    pinMode(kInputPins[i], INPUT_PULLUP);
    const bool active = digitalRead(kInputPins[i]) == LOW;
    inputs[i].begin(active, millis());
    if (active) {
      Serial.print(F("CYCLE_SIM_V1 HELD_AT_BOOT input="));
      Serial.println(i + 1);
    }
  }
  cycle.begin(millis());
  Wire.begin();
  Wire.setClock(100000UL);
  Wire.setWireTimeout(kWireTimeoutUs, true);
  Wire.clearWireTimeoutFlag();
  const int status = lcd.begin(kLcdColumns, kLcdRows);
  if (status == 0 && !Wire.getWireTimeoutFlag()) {
    lcdReady = true;
  } else {
    displayFault(F("begin"), status != 0 ? status : -2);
  }
  const uint32_t now = millis();
  drawSimulation(now);
  printStatus(now);
  Serial.println(F("CYCLE_SIM_V1 READY: index15s, SIM warmup5s/cook10s; basket untested."));
  Serial.println(F("Physical flavor button starts; hand-operate matching index. Busy presses ignored."));
  Serial.println(F("? prints status; r resets/abandons this software simulation only."));
  lastStatusMs = now;
  lastDisplayMs = now;
}

void loop() {
  const uint32_t now = millis();
  // Read all six real contacts before advancing the controller. Never fake
  // index events from elapsed time or accept a wrong index as the selected one.
  uint8_t buttonPresses = 0;
  uint8_t activeIndexes = 0;
  for (uint8_t i = 0; i < kInputCount; ++i) {
    const bool active = digitalRead(kInputPins[i]) == LOW;
    const ButtonEvent event = inputs[i].update(active, now);
    if (event != ButtonEvent::None) {
      Serial.print(F("CYCLE_SIM_V1 CONTACT input="));
      Serial.print(i + 1);
      Serial.print(F(" state="));
      Serial.println(active ? F("ACTIVE") : F("RELEASED"));
    }
    if (i < 3 && event == ButtonEvent::Pressed) buttonPresses |= uint8_t(1U << i);
    if (i >= 3 && inputs[i].stablePressed) activeIndexes |= uint8_t(1U << (i - 3));
  }

  // A serial bench reset clears controller state, not contact filters: a
  // button already held remains disarmed until released and pressed again.
  bool resetRequested = false;
  if (Serial.available() > 0) {
    const char command = char(Serial.read());
    if (command == 'r') resetRequested = true;
    if (command == '?') printStatus(now);
  }
  const CyclePhase previous = cycle.phase();
  if (resetRequested) {
    cycle.begin(now);
    Serial.println(F("CYCLE_SIM_V1 EXPLICIT_BENCH_RESET: no physical stop function"));
  } else {
    if (buttonPresses != 0 && previous != CyclePhase::Idle) {
      Serial.print(F("CYCLE_SIM_V1 IGNORED_BUSY button_mask="));
      Serial.println(buttonPresses);
    }
    cycle.update(now, activeIndexes, buttonPresses);
  }
  if (cycle.phase() != previous) {
    Serial.print(F("CYCLE_SIM_V1 PHASE "));
    Serial.print(phaseName(previous));
    Serial.print(F(" -> "));
    Serial.println(phaseName(cycle.phase()));
    printStatus(now);
  }
  if (cycle.phase() != previous || now - lastDisplayMs >= kDisplayIntervalMs) {
    drawSimulation(now);
    lastDisplayMs = now;
  }
  if (now - lastStatusMs >= kStatusIntervalMs) {
    printStatus(now);
    lastStatusMs = now;
  }
  digitalWrite(LED_BUILTIN, lcdReady ? ((now / 1000UL) % 2UL) : HIGH);
}

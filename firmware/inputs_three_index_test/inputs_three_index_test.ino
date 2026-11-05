/*
 * Fries machine — three flavor buttons plus three index switches / LCD diagnostic, version 1.
 * Mega 2560, Arduino AVR Boards 1.8.8, hd44780 by Bill Perry 1.3.2.
 *
 * Wiring, matching docs/WIRING.md:
 *   LCD: GND->GND, VCC->5V, SDA->20, SCL->21, measured address 0x27.
 *   Button 1: digital 22 and GND; button 2: 23/GND; button 3: 24/GND.
 *   Index 1/2/3: NO->26/28/30 respectively; each COM->common GND.
 *   All three NC terminals stay disconnected. Shared ground is signal-only.
 * USB power only. No motors, drivers, relay or heater connected.
 *
 * Each stable actuation increments its own counter. Each index shows
 * ACTIVE/READY as the lever is actuated/released. A hold counts only once.
 * An input held at boot shows its real state but needs release before its
 * first counted press. These are input checks, not motor/homing controls.
 */

#include <Arduino.h>
#include <Wire.h>
#include <stdio.h>
#include <string.h>
#include <hd44780.h>
#include <hd44780ioClass/hd44780_I2Cexp.h>
#include "ButtonInput.h"

#if !defined(ARDUINO_AVR_MEGA2560)
#error "Use arduino:avr:mega:cpu=atmega2560"
#endif

// Keep the input pins separate from the LCD/USB serial/onboard LED pins.
constexpr uint8_t kInputCount = 6;
constexpr uint8_t kInputPins[kInputCount] = {22, 23, 24, 26, 28, 30};
// Array positions0-2 are buttons1-3; positions3-5 are index switches1-3.
constexpr uint8_t kFirstIndexInput = 3;
constexpr uint8_t kIndexCount = 3;
static_assert(kFirstIndexInput + kIndexCount == kInputCount, "Input groups must fit");
static_assert(kInputPins[3] == 26 && kInputPins[4] == 28 && kInputPins[5] == 30,
              "Index pins must match NO26/28/30 and shared COM/GND wiring");
constexpr uint8_t kLcdAddress = 0x27;
constexpr uint8_t kLcdColumns = 16;
constexpr uint8_t kLcdRows = 2;
constexpr unsigned long kSerialBaud = 115200UL;
constexpr unsigned long kStatusIntervalMs = 2000UL;
constexpr uint32_t kWireTimeoutUs = 25000UL;
static_assert(SDA == 20 && SCL == 21, "LCD must use Mega SDA20/SCL21");

hd44780_I2Cexp lcd(kLcdAddress);
ButtonInput inputs[kInputCount];
unsigned long pressCounts[kInputCount] = {0};
bool lcdReady = false;
unsigned long lastStatusMs = 0;

void displayFault(const __FlashStringHelper* stage, int status) {
  lcdReady = false;  // Stop further display writes; retain input serial logs.
  Serial.print(F("INPUTS_3INDEX_V1 LCD_ERROR stage="));
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

// READY means lever released, not oil/motor readiness. LOW closes NO to GND.
void showIndexState(uint8_t input) {
  // Each index gets its own number, debounced state and actuation count.
  if (input < kFirstIndexInput || input >= kInputCount) {
    return;
  }
  char line[kLcdColumns + 1];
  const unsigned indexNumber = unsigned(input - kFirstIndexInput + 1);
  snprintf(line, sizeof(line), "INDEX %u: %s", indexNumber,
           inputs[input].stablePressed ? "ACTIVE" : "READY");
  if (!writeLcdLine(0, line)) {
    return;
  }
  snprintf(line, sizeof(line), "Count:%10lu", pressCounts[input]);
  writeLcdLine(1, line);
}

void printInputStatus() {
  Serial.print(F("INPUTS_3INDEX_V1 STATUS raw="));
  // HIGH (1) is released; LOW (0) is pressed with these pull-up inputs.
  for (uint8_t i = 0; i < kInputCount; ++i) {
    Serial.print(digitalRead(kInputPins[i]));
  }
  Serial.print(F(" counts="));
  for (uint8_t i = 0; i < kInputCount; ++i) {
    if (i > 0) {
      Serial.print(',');
    }
    Serial.print(pressCounts[i]);
  }
  Serial.print(F(" lcd="));
  Serial.println(lcdReady ? F("OK") : F("FAULT"));
}

void recordPress(uint8_t index) {
  // Keep separate counters for flavor buttons1-3 and index switches1-3.
  ++pressCounts[index];
  Serial.print(F("INPUTS_3INDEX_V1 PRESS input="));
  Serial.print(index + 1);
  Serial.print(F(" pin="));
  Serial.print(kInputPins[index]);
  Serial.print(F(" count="));
  Serial.println(pressCounts[index]);

  if (index >= kFirstIndexInput) {
    showIndexState(index);
    return;
  }
  // Button presses still show FLAVOR 1/2/3 and that button's own count.
  // The next index transition returns the LCD to the live switch state.
  char line[kLcdColumns + 1];
  snprintf(line, sizeof(line), "FLAVOR %u", unsigned(index + 1));
  if (!writeLcdLine(0, line)) {
    return;
  }
  // Six label characters plus a ten-character count fill all 16 columns.
  snprintf(line, sizeof(line), "Count:%10lu", pressCounts[index]);
  writeLcdLine(1, line);
}

void setup() {
  digitalWrite(LED_BUILTIN, LOW);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(kSerialBaud);
  Serial.println(F("INPUTS_3INDEX_V1 boot: buttons22,23,24 index26,28,30; LCD0x27 SDA20 SCL21"));

  // INPUT_PULLUP enables a weak internal resistor to 5V, so contacts require
  // only a connection from their input to GND. Never wire these contacts to 12V.
  for (uint8_t i = 0; i < kInputCount; ++i) {
    pinMode(kInputPins[i], INPUT_PULLUP);
  }
  for (uint8_t i = 0; i < kInputCount; ++i) {
    const bool heldAtBoot = digitalRead(kInputPins[i]) == LOW;
    inputs[i].begin(heldAtBoot, millis());
    if (heldAtBoot) {
      Serial.print(F("INPUTS_3INDEX_V1 HELD_AT_BOOT input="));
      Serial.print(i + 1);
      Serial.println(F(" release before use"));
    }
  }

  Wire.begin();
  Wire.setClock(100000UL);
  Wire.setWireTimeout(kWireTimeoutUs, true);
  Wire.clearWireTimeoutFlag();
  const int beginStatus = lcd.begin(kLcdColumns, kLcdRows);
  if (beginStatus == 0 && !Wire.getWireTimeoutFlag()) {
    lcdReady = true;
    showIndexState(kFirstIndexInput);  // Initial view: index1; serial covers all.
  } else {
    displayFault(F("begin"), beginStatus != 0 ? beginStatus : -2);
  }

  Serial.println(F("INPUTS_3INDEX_V1 READY: 35ms debounce, hold counts once."));
  Serial.println(F("Inputs1-3=buttons; input4=INDEX1/26,5=INDEX2/28,6=INDEX3/30."));
  Serial.println(F("NO contact: released=1/READY; actuated=0/ACTIVE."));
  Serial.println(F("Operate one contact at a time. ? reports actual inputs."));
  printInputStatus();
  lastStatusMs = millis();
}

void loop() {
  const unsigned long nowMs = millis();
  for (uint8_t i = 0; i < kInputCount; ++i) {
    const bool pressed = digitalRead(kInputPins[i]) == LOW;
    const ButtonEvent event = inputs[i].update(pressed, nowMs);
    if (event == ButtonEvent::Pressed) {
      recordPress(i);
    } else if (event == ButtonEvent::Released) {
      Serial.print(F("INPUTS_3INDEX_V1 RELEASE input="));
      Serial.println(i + 1);
      if (i >= kFirstIndexInput) {
        showIndexState(i);  // Release changes ACTIVE to READY without counting.
      }
    }
  }

  // Status allows checking actual pin states without faking button events.
  if (Serial.available() > 0 && Serial.read() == '?') {
    printInputStatus();
  }
  if (nowMs - lastStatusMs >= kStatusIntervalMs) {
    lastStatusMs = nowMs;
    printInputStatus();
  }
  digitalWrite(LED_BUILTIN, lcdReady ? ((nowMs / 1000UL) % 2UL) : HIGH);
}

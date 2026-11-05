/*
 * Fries machine — three flavor-button / LCD diagnostic, version 1.
 * Mega 2560, Arduino AVR Boards 1.8.8, hd44780 by Bill Perry 1.3.2.
 *
 * Wiring, matching docs/WIRING.md:
 *   LCD: GND->GND, VCC->5V, SDA->20, SCL->21, measured address 0x27.
 *   Button 1: digital 22 and GND; button 2: 23/GND; button 3: 24/GND.
 * USB power only. No motors, drivers, relay or heater connected.
 *
 * Each debounced press updates the display and increments that button's
 * own counter. A held button counts once; release before pressing again.
 * This checks input wiring, not dispensing, cooking or busy-cycle lockout.
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
constexpr uint8_t kButtonCount = 3;
constexpr uint8_t kButtonPins[kButtonCount] = {22, 23, 24};
constexpr uint8_t kLcdAddress = 0x27;
constexpr uint8_t kLcdColumns = 16;
constexpr uint8_t kLcdRows = 2;
constexpr unsigned long kSerialBaud = 115200UL;
constexpr unsigned long kStatusIntervalMs = 2000UL;
constexpr uint32_t kWireTimeoutUs = 25000UL;
static_assert(SDA == 20 && SCL == 21, "LCD must use Mega SDA20/SCL21");

hd44780_I2Cexp lcd(kLcdAddress);
ButtonInput buttons[kButtonCount];
unsigned long pressCounts[kButtonCount] = {0, 0, 0};
bool lcdReady = false;
unsigned long lastStatusMs = 0;

void displayFault(const __FlashStringHelper* stage, int status) {
  lcdReady = false;  // Stop further display writes; retain input serial logs.
  Serial.print(F("FLAVOR_BUTTONS_V1 LCD_ERROR stage="));
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

void printInputStatus() {
  Serial.print(F("FLAVOR_BUTTONS_V1 STATUS raw="));
  // HIGH (1) is released; LOW (0) is pressed with these pull-up inputs.
  for (uint8_t i = 0; i < kButtonCount; ++i) {
    Serial.print(digitalRead(kButtonPins[i]));
  }
  Serial.print(F(" counts="));
  for (uint8_t i = 0; i < kButtonCount; ++i) {
    if (i > 0) {
      Serial.print(',');
    }
    Serial.print(pressCounts[i]);
  }
  Serial.print(F(" lcd="));
  Serial.println(lcdReady ? F("OK") : F("FAULT"));
}

void recordPress(uint8_t index) {
  // Each counter belongs to one button, rather than counting all together.
  ++pressCounts[index];
  Serial.print(F("FLAVOR_BUTTONS_V1 PRESS button="));
  Serial.print(index + 1);
  Serial.print(F(" pin="));
  Serial.print(kButtonPins[index]);
  Serial.print(F(" count="));
  Serial.println(pressCounts[index]);

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
  Serial.println(F("FLAVOR_BUTTONS_V1 boot: inputs22,23,24; LCD0x27 SDA20 SCL21"));

  // INPUT_PULLUP enables a weak internal resistor to 5V, so buttons require
  // only a connection from their input to GND. Never wire a button to 12V.
  for (uint8_t i = 0; i < kButtonCount; ++i) {
    pinMode(kButtonPins[i], INPUT_PULLUP);
  }
  for (uint8_t i = 0; i < kButtonCount; ++i) {
    const bool heldAtBoot = digitalRead(kButtonPins[i]) == LOW;
    buttons[i].begin(heldAtBoot, millis());
    if (heldAtBoot) {
      Serial.print(F("FLAVOR_BUTTONS_V1 HELD_AT_BOOT button="));
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
    if (writeLcdLine(0, "BUTTON TEST")) {
      writeLcdLine(1, "Press 1, 2 or 3");
    }
  } else {
    displayFault(F("begin"), beginStatus != 0 ? beginStatus : -2);
  }

  Serial.println(F("FLAVOR_BUTTONS_V1 READY: 35ms debounce, hold counts once."));
  Serial.println(F("Press one physical button at a time. ? prints input status."));
  printInputStatus();
  lastStatusMs = millis();
}

void loop() {
  const unsigned long nowMs = millis();
  for (uint8_t i = 0; i < kButtonCount; ++i) {
    const bool pressed = digitalRead(kButtonPins[i]) == LOW;
    const ButtonEvent event = buttons[i].update(pressed, nowMs);
    if (event == ButtonEvent::Pressed) {
      recordPress(i);
    } else if (event == ButtonEvent::Released) {
      Serial.print(F("FLAVOR_BUTTONS_V1 RELEASE button="));
      Serial.println(i + 1);
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

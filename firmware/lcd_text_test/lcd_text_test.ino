/*
 * Fries machine — 16x2 LCD text test, version 1.
 *
 * Mega 2560 / Arduino AVR Boards 1.8.8 / hd44780 by Bill Perry 1.3.2.
 * USB-only power. LCD GND->GND, VCC->5V, SDA->20, SCL->21.
 * Backpack address 0x27 was measured by the address scanner, not guessed.
 * Keep motors, drivers, buttons and all other supplies disconnected.
 *
 * This is a display diagnostic, not machine-control firmware.
 */

#include <Arduino.h>
#include <Wire.h>
#include <stdio.h>
#include <hd44780.h>
#include <hd44780ioClass/hd44780_I2Cexp.h>

#if !defined(ARDUINO_AVR_MEGA2560)
#error "Use arduino:avr:mega:cpu=atmega2560"
#endif

constexpr uint8_t kLcdAddress = 0x27;
constexpr uint8_t kLcdColumns = 16;
constexpr uint8_t kLcdRows = 2;
constexpr uint8_t kSdaPin = 20;
constexpr uint8_t kSclPin = 21;
constexpr unsigned long kSerialBaud = 115200UL;
constexpr unsigned long kUpdateIntervalMs = 1000UL;
constexpr uint32_t kWireTimeoutUs = 25000UL;

static_assert(SDA == kSdaPin, "SDA must match wiring pin 20");
static_assert(SCL == kSclPin, "SCL must match wiring pin 21");

// The library discovers the expander-to-LCD internal pin mapping at this
// measured address, avoiding an assumed mapping for the generic backpack.
hd44780_I2Cexp lcd(kLcdAddress);
bool lcdReady = false;
unsigned long lastUpdateMs = 0;

void reportFailure(const __FlashStringHelper* stage, int status) {
  lcdReady = false;  // Stop further LCD writes after any reported fault.
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.print(F("LCD_TEXT_TEST_V1 ERROR stage="));
  Serial.print(stage);
  Serial.print(F(" status="));
  Serial.println(status);
  Serial.println(F("Disconnect USB before checking wires. No automatic retry."));
}

bool writeSeconds(unsigned long seconds) {
  // A 16-column line needs 17 bytes, including the string-ending zero byte.
  // millis()/1000 fits in the eight-character field. Padding replaces old
  // characters without clearing the whole screen and causing flicker.
  char line[kLcdColumns + 1];
  snprintf(line, sizeof(line), "Seconds:%8lu", seconds);

  // Row/column numbering starts at zero: (0,1) is start of the second row.
  const int cursorStatus = lcd.setCursor(0, 1);
  if (cursorStatus != 0) {
    reportFailure(F("row2-cursor"), cursorStatus);
    return false;
  }
  if (lcd.print(line) != kLcdColumns) {
    reportFailure(F("row2-write"), -1);
    return false;
  }
  if (Wire.getWireTimeoutFlag()) {
    reportFailure(F("I2C-timeout"), -2);
    return false;
  }
  return true;
}

void setup() {
  digitalWrite(LED_BUILTIN, LOW);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(kSerialBaud);
  Serial.println(F("LCD_TEXT_TEST_V1 boot: address=0x27, 16x2, SDA20 SCL21"));

  Wire.begin();
  Wire.setClock(100000UL);
  Wire.setWireTimeout(kWireTimeoutUs, true);
  Wire.clearWireTimeoutFlag();

  // begin() checks/initialises the display and enables its backlight.
  // A nonzero status is an error; do not claim success just from address ACK.
  const int beginStatus = lcd.begin(kLcdColumns, kLcdRows);
  if (beginStatus != 0) {
    reportFailure(F("begin"), beginStatus);
    return;
  }
  if (Wire.getWireTimeoutFlag()) {
    reportFailure(F("begin-timeout"), -2);
    return;
  }

  const int cursorStatus = lcd.setCursor(0, 0);
  if (cursorStatus != 0) {
    reportFailure(F("row1-cursor"), cursorStatus);
    return;
  }
  // Exactly 16 characters, including spaces, fill the first row.
  if (lcd.print(F("FRIES MACHINE   ")) != kLcdColumns) {
    reportFailure(F("row1-write"), -1);
    return;
  }
  if (!writeSeconds(millis() / 1000UL)) {
    return;
  }

  lcdReady = true;
  lastUpdateMs = millis();
  Serial.println(F("LCD_TEXT_TEST_V1 READY: confirm readable title and seconds."));
}

void loop() {
  if (!lcdReady) {
    return;  // Failure message remains on serial; no repeated bus operations.
  }
  const unsigned long nowMs = millis();
  // Unsigned subtraction stays valid across the millis() rollover.
  if (nowMs - lastUpdateMs < kUpdateIntervalMs) {
    return;
  }
  lastUpdateMs = nowMs;
  const unsigned long seconds = nowMs / 1000UL;
  if (!writeSeconds(seconds)) {
    return;
  }

  digitalWrite(LED_BUILTIN, (seconds % 2UL) ? HIGH : LOW);
  Serial.print(F("LCD_TEXT_TEST_V1 seconds="));
  Serial.println(seconds);
}

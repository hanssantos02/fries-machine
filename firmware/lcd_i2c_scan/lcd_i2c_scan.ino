/*
 * Fries machine — LCD backpack address check, version 1.
 * Prepared for the next software checkpoint; do not upload before that step.
 *
 * Board: Arduino Mega 2560, Arduino AVR Boards 1.8.8.
 * Wiring: LCD GND -> GND, VCC -> 5V, SDA -> 20, SCL -> 21.
 * USB is the only power source. Keep all other devices disconnected.
 *
 * This checks which I2C address acknowledges the Mega. It does not initialise
 * the character display or prove that its text/backlight functions work.
 * Uses only Wire, included with the installed board core; no library install.
 */

#include <Arduino.h>
#include <Wire.h>

#if !defined(ARDUINO_AVR_MEGA2560)
#error "Use arduino:avr:mega:cpu=atmega2560"
#endif

constexpr uint8_t kSdaPin = 20;
constexpr uint8_t kSclPin = 21;
constexpr unsigned long kSerialBaud = 115200UL;
constexpr unsigned long kBusClockHz = 100000UL;
constexpr uint32_t kWireTimeoutUs = 25000UL;
constexpr uint8_t kFirstAddress = 0x08;
constexpr uint8_t kLastAddress = 0x77;

// Keep the code's connections tied to the Mega board definition.
static_assert(SDA == kSdaPin, "Mega SDA must match wiring pin 20");
static_assert(SCL == kSclPin, "Mega SCL must match wiring pin 21");

void printHexAddress(uint8_t address) {
  Serial.print(F("0x"));
  if (address < 0x10) {
    Serial.print('0');
  }
  Serial.print(address, HEX);
}

void scanBus() {
  Serial.println(F("LCD_I2C_SCAN_V1 scan start: SDA20 SCL21, 100kHz"));

  // Both I2C lines should be HIGH while idle. Do not keep issuing requests
  // into a bus held LOW by a wiring fault or an unpowered/failed device.
  if (digitalRead(kSdaPin) == LOW || digitalRead(kSclPin) == LOW) {
    Serial.print(F("ERROR: bus held LOW; SDA="));
    Serial.print(digitalRead(kSdaPin));
    Serial.print(F(" SCL="));
    Serial.println(digitalRead(kSclPin));
    Serial.println(F("Disconnect USB, check wiring. No automatic retry."));
    return;
  }

  uint8_t found = 0;
  // Reserved I2C addresses are skipped. No application data is written.
  for (uint8_t address = kFirstAddress; address <= kLastAddress; ++address) {
    Wire.clearWireTimeoutFlag();
    Wire.beginTransmission(address);
    const uint8_t result = Wire.endTransmission();

    // Wire's timeout prevents a broken bus from freezing this diagnostic.
    if (Wire.getWireTimeoutFlag()) {
      Serial.print(F("ERROR: I2C timeout at "));
      printHexAddress(address);
      Serial.println(F("; scan stopped. Disconnect USB and check wiring."));
      return;
    }

    if (result == 0) {
      ++found;
      Serial.print(F("FOUND "));
      printHexAddress(address);
      Serial.println();
    } else if (result != 2) {
      // 2 means no acknowledgement at that address, normal during a scan.
      // Other errors are reported instead of claiming a successful scan.
      Serial.print(F("ERROR: Wire status="));
      Serial.print(result);
      Serial.print(F(" at "));
      printHexAddress(address);
      Serial.println(F("; scan stopped. Disconnect USB and check wiring."));
      return;
    }
  }

  Serial.print(F("SCAN_COMPLETE devices="));
  Serial.println(found);
  if (found == 0) {
    Serial.println(F("No address found. Power off before checking connections."));
  }
  Serial.println(F("Send r to repeat. Address ACK alone does not test LCD text."));
}

void setup() {
  Serial.begin(kSerialBaud);
  Wire.begin();  // Mega hardware I2C uses SDA20 and SCL21.
  Wire.setClock(kBusClockHz);
  Wire.setWireTimeout(kWireTimeoutUs, true);

  // Short startup settling time for the USB-powered module, not a cook timer.
  delay(500);
  Serial.println(F("LCD_I2C_SCAN_V1 boot: Mega2560, USB-only LCD test"));
  scanBus();
}

void loop() {
  // Scan once at startup; only a deliberate command starts another scan.
  if (Serial.available() > 0) {
    const int command = Serial.read();
    if (command == 'r' || command == 'R') {
      scanBus();
    }
  }
}

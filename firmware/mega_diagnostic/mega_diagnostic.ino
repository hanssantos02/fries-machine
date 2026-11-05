/*
 * Automatic Fries Machine — bare Mega diagnostic, version 1.
 *
 * Run only on the Mega 2560 with ALL external components disconnected.
 * USB supplies the board. No motor, driver, LCD or external supply is used.
 *
 * Purpose:
 *   1. Show that our newly uploaded program is executing, using a distinctive
 *      pair of short flashes followed by a pause on the built-in L LED.
 *   2. Send a readable heartbeat over USB serial at 115200 baud.
 *   3. Answer '?' from the serial terminal, allowing a receive-path check.
 *
 * Uses Arduino AVR Boards 1.8.8, no additional libraries.
 * Board target: arduino:avr:mega:cpu=atmega2560.
 * This is a controller diagnostic, not machine-control firmware.
 */

#include <Arduino.h>

// Refuse to build for an accidentally selected Uno, ESP32 or other target.
#if !defined(ARDUINO_AVR_MEGA2560)
#error "Select the Mega 2560: arduino:avr:mega:cpu=atmega2560"
#endif

// Configuration: LED_BUILTIN is digital pin 13 in the Mega board definition.
// Leave pin 13 and all other headers empty during this test.
constexpr uint8_t kStatusLedPin = LED_BUILTIN;
constexpr unsigned long kSerialBaud = 115200UL;
constexpr unsigned long kFlashCycleMs = 2000UL;
constexpr unsigned long kFlashOnMs = 120UL;
constexpr unsigned long kSecondFlashStartMs = 240UL;
constexpr unsigned long kHeartbeatIntervalMs = 1000UL;

unsigned long lastHeartbeatMs = 0;
unsigned long heartbeatCount = 0;

// Each 2-second frame has light ON at 0–119 ms and 240–359 ms.
// millis() measures time since startup. This non-blocking pattern keeps the
// processor available for serial handling between LED changes.
void updateStatusLed(unsigned long nowMs) {
  const unsigned long phaseMs = nowMs % kFlashCycleMs;
  const bool firstFlash = phaseMs < kFlashOnMs;
  const bool secondFlash = phaseMs >= kSecondFlashStartMs &&
                           phaseMs < kSecondFlashStartMs + kFlashOnMs;
  digitalWrite(kStatusLedPin, (firstFlash || secondFlash) ? HIGH : LOW);
}

// A heartbeat is a regularly repeated message showing that the loop still runs.
void sendHeartbeat(unsigned long nowMs) {
  // Unsigned subtraction handles millis() wrapping after roughly 50 days.
  if (nowMs - lastHeartbeatMs < kHeartbeatIntervalMs) {
    return;
  }
  lastHeartbeatMs = nowMs;
  ++heartbeatCount;

  // F() stores constant text in program memory instead of scarce working RAM.
  Serial.print(F("FRIES_MEGA_DIAGNOSTIC_V1 heartbeat="));
  Serial.print(heartbeatCount);
  Serial.print(F(" uptime_ms="));
  Serial.println(nowMs);
}

void handleSerialInput() {
  // Limit work per loop pass so a continuous stream cannot starve the LED.
  if (Serial.available() > 0) {
    const int received = Serial.read();
    if (received == '?') {
      Serial.println(F("FRIES_MEGA_DIAGNOSTIC_V1 ACK: USB serial receive OK"));
    }
    // Newline/other characters are intentionally ignored by this diagnostic.
  }
}

void setup() {
  // Set the output latch LOW before enabling the LED output.
  digitalWrite(kStatusLedPin, LOW);
  pinMode(kStatusLedPin, OUTPUT);
  Serial.begin(kSerialBaud);

  // Do not wait for Serial: this board must keep blinking without a terminal.
  // Opening a serial terminal may reset a Mega, so this startup line can repeat.
  Serial.println(F("FRIES_MEGA_DIAGNOSTIC_V1 boot: Mega2560, USB-only test"));
  Serial.println(F("Expected: two short L flashes, pause; heartbeat each second."));
  Serial.println(F("Send ? to check serial receive. Keep external parts disconnected."));
}

void loop() {
  const unsigned long nowMs = millis();
  updateStatusLed(nowMs);
  sendHeartbeat(nowMs);
  handleSerialInput();
}

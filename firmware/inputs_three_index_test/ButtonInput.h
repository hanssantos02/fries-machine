#ifndef FRIES_BUTTON_INPUT_H
#define FRIES_BUTTON_INPUT_H

#include <stdint.h>

// Mechanical contacts can bounce between open/closed for a short time.
// Accept a change only after it has remained stable for this interval.
constexpr uint32_t kButtonDebounceMs = 35UL;

enum class ButtonEvent : uint8_t { None, Pressed, Released };

// This helper uses logical pressed/not-pressed, independent of pin voltage.
// The sketch converts INPUT_PULLUP's LOW reading into pressed=true.
struct ButtonInput {
  bool rawPressed = false;
  bool stablePressed = false;
  bool armed = false;
  uint32_t changedAtMs = 0;

  void begin(bool initialPressed, uint32_t nowMs) {
    rawPressed = initialPressed;
    stablePressed = initialPressed;
    // A button held during startup must be released before it can count.
    armed = !initialPressed;
    changedAtMs = nowMs;
  }

  ButtonEvent update(bool pressed, uint32_t nowMs) {
    if (pressed != rawPressed) {
      rawPressed = pressed;
      changedAtMs = nowMs;
    }
    // Unsigned subtraction preserves timing when millis() wraps around.
    if (uint32_t(nowMs - changedAtMs) < kButtonDebounceMs ||
        stablePressed == rawPressed) {
      return ButtonEvent::None;
    }
    stablePressed = rawPressed;
    if (!stablePressed) {
      armed = true;
      return ButtonEvent::Released;
    }
    if (armed) {
      armed = false;
      return ButtonEvent::Pressed;
    }
    return ButtonEvent::None;
  }
};

#endif

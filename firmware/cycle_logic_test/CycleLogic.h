#ifndef FRIES_CYCLE_LOGIC_H
#define FRIES_CYCLE_LOGIC_H

#include <stdint.h>

// BENCH SIMULATION ONLY. This class has no GPIO, motor or heater interface.
// Real machine warm-up/cook settings and basket movement are not implemented.
struct CycleTiming {
  uint32_t indexTimeoutMs;
  uint32_t warmupMs;
  uint32_t cookMs;
};

enum class CyclePhase : uint8_t { Idle, WaitIndex, Warmup, Cooking, TimersDone, Fault };
enum class CycleFault : uint8_t { None, IndexTimeout, InvalidTiming };

class CycleLogic {
 public:
  explicit CycleLogic(const CycleTiming& timing) : timing_(timing) {}

  // Explicit reset is the only way out of the latched Done/Fault views.
  void begin(uint32_t now) {
    phase_ = validTiming() ? CyclePhase::Idle : CyclePhase::Fault;
    fault_ = validTiming() ? CycleFault::None : CycleFault::InvalidTiming;
    flavor_ = 0;
    enteredAt_ = now;
    indexReleased_ = false;
  }

  // Masks use bits0/1/2 for flavor/index1/2/3 respectively. The index mask
  // contains DEBOUNCED states; button mask contains new debounced press events.
  // A new press while busy is discarded, never queued for a later cycle.
  void update(uint32_t now, uint8_t indexesActive, uint8_t buttonPresses) {
    if (phase_ == CyclePhase::Idle) {
      for (uint8_t candidate = 0; candidate < 3; ++candidate) {
        const uint8_t bit = uint8_t(1U << candidate);
        if ((buttonPresses & bit) != 0) {
          // Deterministic priority if multiple new presses arrive together.
          flavor_ = candidate + 1;
          indexReleased_ = (indexesActive & bit) == 0;
          enter(CyclePhase::WaitIndex, now);
          break;
        }
      }
      return;  // Starting with an already active index cannot complete it.
    }

    const uint32_t elapsed = uint32_t(now - enteredAt_);
    if (phase_ == CyclePhase::WaitIndex) {
      if (elapsed >= timing_.indexTimeoutMs) {
        fault_ = CycleFault::IndexTimeout;
        enter(CyclePhase::Fault, now);  // Deadline wins over a late closure.
        return;
      }
      const uint8_t selectedBit = uint8_t(1U << (flavor_ - 1));
      if ((indexesActive & selectedBit) == 0) {
        indexReleased_ = true;
      } else if (indexReleased_) {
        // Only the selected index, released since start, advances the test.
        enter(CyclePhase::Warmup, now);
      }
    } else if (phase_ == CyclePhase::Warmup && elapsed >= timing_.warmupMs) {
      enter(CyclePhase::Cooking, now);
    } else if (phase_ == CyclePhase::Cooking && elapsed >= timing_.cookMs) {
      // Stop here: basket limits and motion hardware are unavailable.
      enter(CyclePhase::TimersDone, now);
    }
    // Fault and TimersDone remain latched. No automatic retry or new start.
  }

  CyclePhase phase() const { return phase_; }
  CycleFault fault() const { return fault_; }
  uint8_t flavor() const { return flavor_; }
  bool indexReleased() const { return indexReleased_; }

  uint32_t secondsLeft(uint32_t now) const {
    uint32_t duration = 0;
    if (phase_ == CyclePhase::WaitIndex) duration = timing_.indexTimeoutMs;
    if (phase_ == CyclePhase::Warmup) duration = timing_.warmupMs;
    if (phase_ == CyclePhase::Cooking) duration = timing_.cookMs;
    const uint32_t elapsed = uint32_t(now - enteredAt_);
    return elapsed >= duration ? 0 : (duration - elapsed + 999UL) / 1000UL;
  }

 private:
  bool validTiming() const {
    // Keep durations positive and comfortably below a full millis() wrap.
    return timing_.indexTimeoutMs > 0 && timing_.indexTimeoutMs <= 0x7fffffffUL &&
           timing_.warmupMs > 0 && timing_.warmupMs <= 0x7fffffffUL &&
           timing_.cookMs > 0 && timing_.cookMs <= 0x7fffffffUL;
  }
  void enter(CyclePhase next, uint32_t now) {
    phase_ = next;
    enteredAt_ = now;
  }

  CycleTiming timing_;
  CyclePhase phase_ = CyclePhase::Idle;
  CycleFault fault_ = CycleFault::None;
  uint8_t flavor_ = 0;
  uint32_t enteredAt_ = 0;
  bool indexReleased_ = false;
};

#endif

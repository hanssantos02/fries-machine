// Host tests for the same controller and contact filter used on the Mega.
// These exercise control timing, not motors, heating or mechanical delivery.
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include "../cycle_logic_test/CycleLogic.h"
#include "../cycle_logic_test/ButtonInput.h"

const CycleTiming timing = {15000UL, 5000UL, 10000UL};

void selected_index_and_timers() {
  for (uint8_t flavor = 1; flavor <= 3; ++flavor) {
    CycleLogic cycle(timing);
    cycle.begin(0);
    const uint8_t selected = uint8_t(1U << (flavor - 1));
    const uint8_t wrong = uint8_t(1U << (flavor % 3));
    cycle.update(10, 0, selected);
    assert(cycle.phase() == CyclePhase::WaitIndex);
    assert(cycle.flavor() == flavor);
    cycle.update(11, wrong, 7);  // Wrong index and busy presses cannot select.
    assert(cycle.phase() == CyclePhase::WaitIndex);
    assert(cycle.flavor() == flavor);
    cycle.update(20, selected, 7);
    assert(cycle.phase() == CyclePhase::Warmup);
    assert(cycle.secondsLeft(20) == 5);
    assert(cycle.secondsLeft(5019) == 1);
    cycle.update(5019, 0, 7);
    assert(cycle.phase() == CyclePhase::Warmup);
    cycle.update(5020, 0, 7);
    assert(cycle.phase() == CyclePhase::Cooking);
    assert(cycle.flavor() == flavor);
    assert(cycle.secondsLeft(5020) == 10);
    cycle.update(15019, 7, 7);
    assert(cycle.phase() == CyclePhase::Cooking);
    cycle.update(15020, 7, 7);
    assert(cycle.phase() == CyclePhase::TimersDone);
    cycle.update(100000, 0, 7);  // No queued/repeated start after completion.
    assert(cycle.phase() == CyclePhase::TimersDone);
    assert(cycle.flavor() == flavor);
  }
}

void release_timeout_and_reset() {
  CycleLogic cycle(timing);
  cycle.begin(0);
  cycle.update(10, 2, 2);  // Index2 already actuated when button2 starts.
  assert(!cycle.indexReleased());
  cycle.update(1000, 2, 0);
  assert(cycle.phase() == CyclePhase::WaitIndex);
  cycle.update(1001, 0, 0);  // Require release first, then a new actuation.
  assert(cycle.indexReleased());
  cycle.update(1002, 2, 0);
  assert(cycle.phase() == CyclePhase::Warmup);

  cycle.begin(0);
  cycle.update(10, 0, 1);
  cycle.update(15009, 0, 0);
  assert(cycle.phase() == CyclePhase::WaitIndex);
  cycle.update(15010, 1, 7);  // At the exact timeout, fault wins over closure.
  assert(cycle.phase() == CyclePhase::Fault);
  assert(cycle.fault() == CycleFault::IndexTimeout);
  cycle.update(15011, 1, 1);
  assert(cycle.phase() == CyclePhase::Fault);
  cycle.begin(20000);  // Explicit bench reset, never automatic retry.
  assert(cycle.phase() == CyclePhase::Idle);
  assert(cycle.flavor() == 0);
  cycle.update(20001, 0, 6);  // Simultaneous new buttons: lowest number wins.
  assert(cycle.flavor() == 2);

  cycle.begin(0);
  cycle.update(1, 0, 0x80);  // Unrecognised mask bits cannot select a flavor.
  assert(cycle.phase() == CyclePhase::Idle);
}

void configuration_and_rollover() {
  const CycleTiming bad[] = {{0, 5, 10}, {1, 0, 10}, {1, 5, 0},
                            {0x80000000UL, 5, 10}};
  for (const auto& config : bad) {
    CycleLogic invalid(config);
    invalid.begin(0);
    assert(invalid.phase() == CyclePhase::Fault);
    assert(invalid.fault() == CycleFault::InvalidTiming);
  }
  CycleLogic cycle(timing);
  const uint32_t start = 0xfffffff0UL;
  cycle.begin(start);
  cycle.update(start, 0, 1);
  cycle.update(uint32_t(start + 5), 1, 0);
  cycle.update(uint32_t(start + 5004), 0, 0);
  assert(cycle.phase() == CyclePhase::Warmup);
  cycle.update(uint32_t(start + 5005), 0, 0);
  assert(cycle.phase() == CyclePhase::Cooking);
  cycle.update(uint32_t(start + 15005), 0, 0);
  assert(cycle.phase() == CyclePhase::TimersDone);
}

// Real contact filtering feeding the real state machine, without GPIO mocks.
struct InputChain {
  ButtonInput contacts[6];
  CycleLogic cycle;
  explicit InputChain(uint8_t initial = 0) : cycle(timing) {
    for (uint8_t i = 0; i < 6; ++i) {
      contacts[i].begin((initial & (1U << i)) != 0, 0);
    }
    cycle.begin(0);
  }
  void sample(uint32_t now, uint8_t active) {
    uint8_t buttons = 0;
    uint8_t indexes = 0;
    for (uint8_t i = 0; i < 6; ++i) {
      const ButtonEvent event = contacts[i].update((active & (1U << i)) != 0, now);
      if (i < 3 && event == ButtonEvent::Pressed) buttons |= uint8_t(1U << i);
      if (i >= 3 && contacts[i].stablePressed) indexes |= uint8_t(1U << (i - 3));
    }
    cycle.update(now, indexes, buttons);
  }
};

void filtered_input_chain() {
  InputChain chain;
  chain.sample(10, 2);
  chain.sample(20, 0);  // Bounce cannot start a simulation.
  chain.sample(30, 2);
  chain.sample(64, 2);
  assert(chain.cycle.phase() == CyclePhase::Idle);
  chain.sample(65, 2);
  assert(chain.cycle.flavor() == 2);
  chain.sample(70, 10);  // Wrong index1 plus held button2.
  chain.sample(105, 10);
  assert(chain.cycle.phase() == CyclePhase::WaitIndex);
  chain.sample(110, 18); // Correct index2 plus held button2.
  chain.sample(145, 18);
  assert(chain.cycle.phase() == CyclePhase::Warmup);
  chain.sample(5145, 18);
  assert(chain.cycle.phase() == CyclePhase::Cooking);
  chain.sample(15145, 18);
  assert(chain.cycle.phase() == CyclePhase::TimersDone);
  chain.cycle.begin(16000);  // Held button cannot restart even after reset.
  chain.sample(16000, 18);
  assert(chain.cycle.phase() == CyclePhase::Idle);

  InputChain heldAtBoot(1);
  heldAtBoot.sample(100, 1);
  assert(heldAtBoot.cycle.phase() == CyclePhase::Idle);
  heldAtBoot.sample(110, 0);
  heldAtBoot.sample(145, 0);
  heldAtBoot.sample(150, 1);
  heldAtBoot.sample(185, 1);
  assert(heldAtBoot.cycle.phase() == CyclePhase::WaitIndex);
}

int main() {
  selected_index_and_timers();
  release_timeout_and_reset();
  configuration_and_rollover();
  filtered_input_chain();
  puts("PASS: all flavors, selected index, release-before-index, busy lockout, timing boundaries, timeout latch/reset, rollover and real debounce/controller chain.");
}

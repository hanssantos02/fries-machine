// Host-side tests for the same debounce helper used on the Mega.
// These verify time/event behaviour, not physical wires or button operation.
#include <assert.h>
#include <stdio.h>
#include "../flavor_buttons_test/ButtonInput.h"

int main() {
  ButtonInput button;
  button.begin(false, 0);
  assert(button.update(true, 10) == ButtonEvent::None);
  assert(button.update(true, 44) == ButtonEvent::None);
  assert(button.update(true, 45) == ButtonEvent::Pressed);
  assert(button.update(true, 2500) == ButtonEvent::None);  // no held repeat
  assert(button.update(false, 2501) == ButtonEvent::None);
  assert(button.update(false, 2536) == ButtonEvent::Released);
  assert(button.update(true, 3000) == ButtonEvent::None);
  assert(button.update(true, 3035) == ButtonEvent::Pressed);

  button.begin(false, 0);
  assert(button.update(true, 10) == ButtonEvent::None);
  assert(button.update(false, 20) == ButtonEvent::None);
  assert(button.update(true, 25) == ButtonEvent::None);
  assert(button.update(false, 29) == ButtonEvent::None);
  assert(button.update(true, 31) == ButtonEvent::None);
  assert(button.update(true, 65) == ButtonEvent::None);
  assert(button.update(true, 66) == ButtonEvent::Pressed);  // bounce settled
  assert(button.update(true, 1000) == ButtonEvent::None);

  button.begin(true, 0);  // held during boot must not count a new press
  assert(button.update(true, 200) == ButtonEvent::None);
  assert(button.update(false, 210) == ButtonEvent::None);
  assert(button.update(false, 245) == ButtonEvent::Released);
  assert(button.update(true, 260) == ButtonEvent::None);
  assert(button.update(true, 295) == ButtonEvent::Pressed);

  button.begin(false, 0xfffffff0UL);
  assert(button.update(true, 0xfffffff5UL) == ButtonEvent::None);
  assert(button.update(true, 23) == ButtonEvent::None);  // 34 ms after wrap
  assert(button.update(true, 24) == ButtonEvent::Pressed);  // 35 ms

  puts("PASS: debounce, held press, release/repress, startup hold, timer rollover.");
}

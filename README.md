# fries-machine

Automatic Fries Machine — beginner-guided embedded prototype, currently **Phase 2**, not a completed cooking appliance.

## Continue the assembly

Read [the 6 November 2026 handoff](docs/handoffs/2026-11-06-motor-wiring-resume.md), [current assembly checkpoint](docs/ASSEMBLY_CHECKPOINT.md), [project instructions](AGENTS.md), [requirements](PROJECT.md) and [progress](PROGRESS.md). The [5 November handoff](docs/handoffs/2026-11-05-assembly-resume.md) is the earlier adapter-receipt snapshot.

USB logic was reconnected and reported working. Adapter label now shows12VDC5A/centre-positive. One motor supply pair and a taped soldered positive split have been assembled/checked by user report, with fuse removed and power disconnected. **Phase2Step37—motor-positive/banded-diode solder joint—was issued but its completion is unreported.** Current Mega firmware remains output-free simulation; no motor GPIO or powered motor test. No real dispensing, basket movement, heating or safety-stop validation is complete.

- [Materials in hand](docs/INVENTORY.md) and [remaining purchases](docs/REMAINING_PURCHASES.md)
- [Physical-store list](docs/PHYSICAL_STORE_LIST.md), including buzzer/LED components
- [Prototype build](docs/BUILD_PROTOTYPE.md), [wiring](docs/WIRING.md) and [testing](docs/TESTING.md)
- [Session photo evidence](docs/assets/motor-review-2026-11-05/manifest.json) and [wiring-tool guide](docs/TOOLS.md)
- [Current simulation source](firmware/cycle_logic_test/) and [historical bench evidence](docs/evidence/2026-10-28/)
- [Arduino setup](docs/ARDUINO_SETUP.md); local toolchains/builds are excluded from Git. Install/flash permissions and physical-result gates are in AGENTS.md.

Repository: https://github.com/hanssantos02/fries-machine — branch `main`. Prices and workbook are historical planning snapshots, not current quotes or paid totals. The original mechanical PDF remains the design reference.

#!/usr/bin/env bash
# Shared environment, sourced by the two scripts below. No downloads here.
# Keep tool data, build cache and temporary files within this project.
FRIES_PROJECT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
FRIES_ARDUINO_ROOT="$FRIES_PROJECT_ROOT/.tools/arduino"
export ARDUINO_DIRECTORIES_DATA="$FRIES_ARDUINO_ROOT/data"
export ARDUINO_DIRECTORIES_DOWNLOADS="$FRIES_ARDUINO_ROOT/downloads"
export ARDUINO_DIRECTORIES_USER="$FRIES_ARDUINO_ROOT/user"
export ARDUINO_BUILD_CACHE_PATH="$FRIES_ARDUINO_ROOT/build-cache"
export ARDUINO_METRICS_ENABLED=false
export ARDUINO_UPDATER_ENABLE_NOTIFICATION=false
export TMPDIR="$FRIES_ARDUINO_ROOT/tmp"
FRIES_ARDUINO_CLI="$FRIES_ARDUINO_ROOT/bin/arduino-cli"
FRIES_ARDUINO_CONFIG="$FRIES_PROJECT_ROOT/tools/arduino-cli.yaml"

mkdir -p "$ARDUINO_DIRECTORIES_DATA" "$ARDUINO_DIRECTORIES_DOWNLOADS" \
  "$ARDUINO_DIRECTORIES_USER" "$ARDUINO_BUILD_CACHE_PATH" "$TMPDIR" \
  "$FRIES_ARDUINO_ROOT/bin"

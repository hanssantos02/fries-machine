#!/usr/bin/env bash
# Compile is software-only. Upload writes firmware and requires user permission.
# Monitor opens/resets the board; use only with the bare USB-powered Mega.
set -euo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/arduino-env.sh"

if [[ ! -x "$FRIES_ARDUINO_CLI" ]]; then
  echo 'Project-local Arduino CLI missing. Obtain permission for setup first.' >&2
  exit 1
fi

FRIES_FQBN=arduino:avr:mega:cpu=atmega2560
FRIES_SKETCH="$FRIES_PROJECT_ROOT/firmware/mega_diagnostic"
FRIES_BUILD="$FRIES_PROJECT_ROOT/.build/mega_diagnostic"
FRIES_ACTION="${1:-}"
FRIES_PORT="${2:-}"

case "$FRIES_ACTION" in
  compile)
    "$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" compile \
      --fqbn "$FRIES_FQBN" --warnings all --build-path "$FRIES_BUILD" "$FRIES_SKETCH"
    ;;
  list)
    "$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" board list
    ;;
  upload|monitor)
    # A port must be passed deliberately; never silently choose the first device.
    if [[ -z "$FRIES_PORT" || ! -c "$FRIES_PORT" || ! -r "$FRIES_PORT" || ! -w "$FRIES_PORT" ]]; then
      echo 'Supply the verified, readable/writable Mega serial device as argument 2.' >&2
      exit 1
    fi
    if [[ "$FRIES_ACTION" == upload ]]; then
      if [[ ! -s "$FRIES_BUILD/mega_diagnostic.ino.hex" ]]; then
        echo 'No compiled diagnostic binary. Compile successfully before upload.' >&2
        exit 1
      fi
      "$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" upload \
        --fqbn "$FRIES_FQBN" --port "$FRIES_PORT" \
        --input-dir "$FRIES_BUILD" --verify "$FRIES_SKETCH"
    else
      "$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" monitor \
        --port "$FRIES_PORT" --config baudrate=115200
    fi
    ;;
  *)
    echo 'Usage: bash tools/mega-diagnostic.sh compile|list|upload|monitor [verified-port]' >&2
    exit 2
    ;;
esac

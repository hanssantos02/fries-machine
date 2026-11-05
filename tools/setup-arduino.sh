#!/usr/bin/env bash
# Requires user permission before execution: downloads/installs build tools.
# It does not upload to a board or alter Linux groups/system packages.
set -euo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/arduino-env.sh"

if [[ "$(uname -m)" != x86_64 || "$(uname -s)" != Linux ]]; then
  echo 'This pinned CLI archive is for Linux x86_64 only.' >&2
  exit 1
fi
for fries_command in curl tar sha256sum; do
  command -v "$fries_command" >/dev/null || {
    echo "Required command unavailable: $fries_command" >&2
    exit 1
  }
done

FRIES_CLI_ARCHIVE=arduino-cli_1.5.1_Linux_64bit.tar.gz
curl --fail --location --retry 2 --connect-timeout 20 \
  --output "$ARDUINO_DIRECTORIES_DOWNLOADS/$FRIES_CLI_ARCHIVE" \
  "https://github.com/arduino/arduino-cli/releases/download/v1.5.1/$FRIES_CLI_ARCHIVE"
(
  cd "$ARDUINO_DIRECTORIES_DOWNLOADS"
  sha256sum --check "$FRIES_PROJECT_ROOT/tools/arduino-cli.sha256"
)
tar --extract --gzip --file "$ARDUINO_DIRECTORIES_DOWNLOADS/$FRIES_CLI_ARCHIVE" \
  --directory "$FRIES_ARDUINO_ROOT/bin" arduino-cli

"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" version
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" core update-index
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" core install arduino:avr@1.8.8
"$FRIES_ARDUINO_CLI" --config-file "$FRIES_ARDUINO_CONFIG" core list

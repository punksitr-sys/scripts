#!/bin/bash
if [[ $# -lt 2 ]]; then
    echo "Usage: fk <offset_hours> <command...>"
    exit 1
fi

if ! command -v faketime &>/dev/null; then
    echo "[!] faketime not found, please install it first."
    exit 1
fi

OFFSET="$1"
shift
TARGET_TIME=$(date -u -d "$OFFSET hours" +"%Y-%m-%d %H:%M:%S")
echo "[*] Faketime set to UTC: $TARGET_TIME"
exec faketime "$TARGET_TIME" "$@"

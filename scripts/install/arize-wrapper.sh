#!/usr/bin/env bash
# arize-wrapper.sh — symlinked to ~/.local/bin/arize.
# Activates the managed venv and execs the real arize CLI.

ARIZE_HOME="${ARIZE_HOME:-$HOME/.arize}"
VENV="$ARIZE_HOME/.venv"

if [[ ! -d "$VENV" ]]; then
    echo "arize: venv not found at $VENV" >&2
    echo "Re-run the installer: curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash" >&2
    exit 1
fi

exec "$VENV/bin/arize" "$@"

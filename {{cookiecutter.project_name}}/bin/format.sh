#!/usr/bin/env bash

set -eo pipefail
cd "$(dirname "$0")/.."

uv run black src
uv run black tests

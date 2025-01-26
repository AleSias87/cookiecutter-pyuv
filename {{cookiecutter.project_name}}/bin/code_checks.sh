#!/usr/bin/env bash

set -eo pipefail
cd "$(dirname "$0")/.."

uv run ruff check
uv run ruff format --check
echo
uv run mypy

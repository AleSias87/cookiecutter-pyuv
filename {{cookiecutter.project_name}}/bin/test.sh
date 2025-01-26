#!/usr/bin/env bash

set -eo pipefail
cd "$(dirname "$0")/.."

uv run pytest --cov=src/ tests/

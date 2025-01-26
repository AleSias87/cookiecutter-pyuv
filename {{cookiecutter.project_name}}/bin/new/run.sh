#!/usr/bin/env bash

#? Creates a new Python file

set -eo pipefail

usage() {
  echo "Usage: $0 [file_name.py ^| folder_name]"
  exit 1
}

if [ -z "$1" ]; then
  echo "Error: No argument provided."
  usage
fi

uv run "$(dirname "$0")/new.py" $@

# Copyright (C) 2025  Alessandro Sias
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""The script creates a new Python file (or a folder with __init__.py) with the
license header.
"""

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).parent / "../../src/{{cookiecutter.project_slug}}"


def main(path: Path) -> None:
    """Creates a new Python file.

    Parameters
    ----------
    path : Path
        The relative path where create the file. The root is always the project
        folder.
    """

    match path.suffix:
        case ".py":
            _new_file(_PROJECT_ROOT / path)

        case "":
            (_PROJECT_ROOT / path).mkdir(parents=True, exist_ok=True)
            _new_file(_PROJECT_ROOT / path / "__init__.py")

        case _:
            print(f"{_print_err()} Only *.py files can be created")


def _new_file(path: Path) -> None:
    if path.exists():
        print(f"{_print_err()} {path.resolve()} already exists")
        return None

    try:
        with open(Path(__file__).parent / "license_header") as fid:
            license_header = fid.read()
    except FileNotFoundError:
        license_header = ""

    with open(path, "w") as fid:
        _ = fid.write(license_header)

    print(f"✨ {path.resolve()} has been created")
    return None


def _print_err() -> str:
    return "\033[38;5;160;1mError:\033[0m"


if __name__ == "__main__":
    main(Path(sys.argv[1]))

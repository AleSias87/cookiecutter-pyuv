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

"""The cookiecutter pre_gen_project hook."""

import re
import sys


def _check_project_name() -> None:
    project_name_regex = r"^[a-zA-Z][-_a-zA-Z0-9]+$"
    project_name = "{{cookiecutter.project_name}}"

    if not re.match(project_name_regex, project_name):
        print(
            (
                f"{_print_err()} The project name {_print_bold(project_name)} is not a valid name.\n"
                "Valid name must:\n"
                "  * contains only letters, numbers and hyphen\n"
                "  * must starts with a letter"
            )
        )
        sys.exit(1)


def _check_project_slug() -> None:
    project_slug_regex = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
    project_slug = "{{cookiecutter.project_slug}}"
    if not re.match(project_slug_regex, project_slug):
        print(
            (
                f"{_print_err()} The project slug {_print_bold(project_slug)} is not a valid name.\n"
                "Valid name must:\n"
                "  * contains only letters, numbers and underscore\n"
                "  * must starts with a letter or an underscore"
            )
        )
        sys.exit(1)


def _print_err() -> str:
    return "\033[38;5;160;1mError:\033[0m"


def _print_bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"


if __name__ == "__main__":
    _check_project_name()
    _check_project_slug()

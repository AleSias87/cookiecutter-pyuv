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

"""The cookiecutter post_gen_project hook."""

import os
import shutil
import subprocess
from pathlib import Path


def _setup_license(project_path: Path) -> None:
    license_paths = {
        "MIT license": "licenses/mit",
        "BSD license": "licenses/bsd",
        "Apache Software License 2.0": "licenses/apache",
        "GNU General Public License v3": "licenses/gpl",
    }
    for license, rel_path in license_paths.items():
        if license == "{{cookiecutter.open_source_license}}":
            shutil.move(project_path / rel_path / "LICENSE", project_path / "LICENSE")
            shutil.move(project_path / rel_path / "header", project_path / "bin/new/license_header")
            break

    shutil.rmtree(project_path / "licenses")


def _init_uv() -> None:
    _ = subprocess.run("uv run")


def _init_repo() -> None:
    remote = (
        "https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}"
    )
    _ = subprocess.run(
        f"""git init
        git branch -M main
        git remote add origin {remote}
        git push -u origin main
        """,
        shell=True,
    )


def _init_pre_commit(project_path: Path) -> None:
    cmd_path = ".venv/Scripts/pre-commit" if os.name == "nt" else ".venv/bin/pre-commit"
    _ = subprocess.run(f"{project_path / cmd_path} install")


def _init_package(project_path: Path) -> None:
    try:
        with open(project_path / "bin/new/license_header") as fid:
            license_header = fid.read()
    except FileNotFoundError:
        license_header = ""

    with open(project_path / "src/{{cookiecutter.project_slug}}/__init__.py") as fid:
        init_content = fid.read()

    with open(project_path / "src/{{cookiecutter.project_slug}}/__init__.py", "w") as fid:
        _ = fid.write(f"{license_header}\n{init_content}")


def _stylize_print(text: str) -> str:
    return f"\033[38;5;45;1m{text}\033[0m"


if __name__ == "__main__":
    project_path = Path.cwd()
    project_name = "{{cookiecutter.project_name}}"

    _setup_license(project_path)
    _init_repo()
    _init_package(project_path)
    {% if cookiecutter.init_workspace == "y" %}
    _init_uv()
    _init_pre_commit(project_path)
    {% endif %}

    print(
        (
            f"\n✨✨🚀 Initialized project '{_stylize_print(project_name)}' at "
            f"'{_stylize_print(project_path.as_posix())}'"
        )
    )

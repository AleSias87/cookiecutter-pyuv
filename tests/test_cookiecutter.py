# Ignore types because pytest_cookies miss them
# type: ignore
import filecmp
from pathlib import Path

import pytest
from cookiecutter.exceptions import FailedHookException
from pytest_cookies.plugin import Cookies


def test_bake_project(cookies: Cookies) -> None:
    # act
    result = cookies.bake(extra_context={"project_name": "test-project", "init_workspace": "n"})

    # assert
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "test-project"
    assert result.project_path.is_dir()


@pytest.mark.parametrize(
    "extra_content",
    [
        {"project_name": "project_name_not_valid"},
        {"project_name": "3-project-name-not-valid"},
        {"project_slug": "project-slug-not-valid"},
        {"project_slug": "3_project_name_not_valid"},
    ],
)
def test_fails_create_for_invalid_data(cookies: Cookies, extra_content: dict[str, str]) -> None:
    # act
    result = cookies.bake(extra_context={"init_workspace": "n"} | extra_content)

    # assert
    assert result.exit_code == -1
    assert isinstance(result.exception, FailedHookException)


@pytest.mark.parametrize(
    ["license", "path_expected"],
    [
        pytest.param(
            "MIT license", Path("../{{cookiecutter.project_name}}/licenses/mit/LICENSE"), id="mit"
        ),
        pytest.param(
            "BSD license", Path("../{{cookiecutter.project_name}}/licenses/bsd/LICENSE"), id="bsd"
        ),
        pytest.param(
            "Apache Software License 2.0",
            Path("../{{cookiecutter.project_name}}/licenses/apache/LICENSE"),
            id="apache",
        ),
        pytest.param(
            "GNU General Public License v3",
            Path("../{{cookiecutter.project_name}}/licenses/gpl/LICENSE"),
            id="gpl",
        ),
    ],
)
def test_license(cookies: Cookies, license: str, path_expected: Path) -> None:
    # act
    result = cookies.bake(extra_context={"open_source_license": license, "init_workspace": "n"})

    # assert
    assert result.exit_code == 0
    assert result.exception is None
    assert filecmp.cmpfiles(path_expected, result.project_path, "LICENSE")[1] == []


def test_no_license(cookies: Cookies) -> None:
    # act
    result = cookies.bake(
        extra_context={"open_source_license": "Not open source", "init_workspace": "n"}
    )

    # assert
    assert result.exit_code == 0
    assert result.exception is None
    assert not (result.project_path / "LICENSE").is_file()

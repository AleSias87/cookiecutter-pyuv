# {{cookiecutter.project_name}}

[![Release](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/main.yml?branch=main)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Commit activity](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
- **Documentation** <https://{{cookiecutter.author_github_handle}}.github.io/{{cookiecutter.project_name}}/>

## Getting started

[cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/
[uv]: https://docs.astral.sh/uv/
[pytest]: https://pydata-sphinx-theme.readthedocs.io/en/stable/
[black]: https://black.readthedocs.io/en/stable/
[ruff]: https://docs.astral.sh/ruff/
[pyright]: https://microsoft.github.io/pyright/#/
[pylint]: https://pylint.readthedocs.io/en/stable/user_guide/installation/
[codespell]: https://github.com/codespell-project/codespell
[sphinx]: https://www.sphinx-doc.org/en/master/
[pydata-sphinx-theme]: https://pydata-sphinx-theme.readthedocs.io/en/stable/

### 1. Initialize a new project

> [!INFO]
> This steps assumes that you already have installed [cookiecutter] and [uv].
> If these packages are not available, install them before proceed:
> ```bash
> pip install cookiecutter
> pip install uv
> ```

- Create a new project on GitHub
- Run this template from your local machine `cookiecutter gh:AleSias87/cookiecutter-pypa`
providing the same project name just created.

### 2. Development environment

This template initializes by default the local repository setting the remote upstream.

Furthermore, if during the project configuration you choose to initialize also
the workspace, it initialize the development virtual environment as well as the
pre-commit hooks and you're ready to code.

If, instead, the initialization was skipped, it's necessary to build the
virtual environment and initialize the pre-commit hooks manually. To do so

```bash
uv run
pre-commit install
```

The development environment uses:
- [uv] to manage dependencies and build the distribution
- [pytest] for testing
- [black] to format the code
- [ruff], [pyright], [pylint], [codespell] for linting and checking the code
- [sphinx] to write the documentation with [pydata-sphinx-theme]

### uv

Following some basic commands. For more complete overview see the [uv] documentation

```bash
uv add [package_name]  # add [package_name] as project dependencies
uv remove [package_name]  # remove [package_name] from project dependencies
uv build  # build the package project distribution
```

### sphinx

To build the documentation run `docs/make html`

### Other utilities

Inside the `bin` folder of the project are provided some scripts to improve the productivity

```bash
bin/new [file_name.py | folder_name]  # creates a file or a package inside the scr/{project_name} directory with license header
bin/test  # run all tests
bin/code_checks  # run ruff and mypy code checks
bin/format  # run the code formatting with black
```

### 3. Commit the changes

To commit the changes to your repository.

```bash
git add -A
git commit -m "Commit message"
git push
```

To accept the commit the following checks must be passed

```text
check for case conflicts.................................................Passed
check for merge conflicts................................................Passed
check toml...............................................................Passed
check yaml...............................................................Passed
check docstring is first.................................................Passed
fix end of files.........................................................Passed
trim trailing whitespace.................................................Passed
ruff.....................................................................Passed
ruff-format..............................................................Passed
mypy.....................................................................Passed
codespell................................................................Passed
```

### 4. Build a new version

To build a new version change the `version` under `[project]` section of `pyproject.toml` and run `uv build` and `docs/make html`.
The version and documentation package are read from package metadata and is not needed to update the value in other places.

```python
import importlib.metadata as metadata

try:
    version = metadata.version("{{cookiecutter.project_slug}}")
except metadata.PackageNotFoundError:
    version = "bare"
```

---

Repository initiated with [cookiecutter-pyuv](https://github.com/AleSias87/cookiecutter-pyuv).

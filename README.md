# cookiecutter-pyuv

[![Release](https://img.shields.io/github/v/release/AleSias87/cookiecutter-pyuv)](https://img.shields.io/github/v/release/AleSias87/{{cookiecutter.project_name}})
[![Commit activity](https://img.shields.io/github/commit-activity/m/AleSias87/cookiecutter-pyuv)](https://img.shields.io/github/commit-activity/m/AleSias87/cookiecutter-pyuv)
[![License](https://img.shields.io/github/license/AleSias87/cookiecutter-pyuv)](https://img.shields.io/github/license/AleSias87/cookiecutter-pyuv)


- **Github repository**: <https://github.com/AleSias87/cookiecutter-pyuv>

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
[pre-commit]: https://pre-commit.com/
[tox-uv]: https://github.com/tox-dev/tox-uv


This is a [cookiecutter] template to start a Python project with many tools for development, testing, and deployment. It supports the following features:

- [uv] for dependency management and version building
- Testing and coverage with [pytest] and [codecov](https://about.codecov.io/)
- Code quality and checks with [ruff], [pyright], [pylint], [codespell]
- Pre-commit hooks with [pre-commit]
- Formatting code with [black]
- Documentation with [sphinx]
- Compatibility testing for multiple versions of Python with [tox-uv]

### 1. Quickstart

> [!NOTE]
> This steps assumes that you already have installed [cookiecutter] and [uv].
> If these packages are not available, install them before proceed:
> ```bash
> pip install cookiecutter
> pip install uv
> ```

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
cookiecutter gh:AleSias87/cookiecutter-pyuv
```

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created. This template initialize the local repository setting the remote upstream and if you want install and initialize the development virtual environment as well as the pre-commit hook and at the end you are ready to code.

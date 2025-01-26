"The {{cookiecutter.project_name}} package version."

import importlib.metadata as metadata

try:
    version = metadata.version("{{cookiecutter.project_slug}}")
except metadata.PackageNotFoundError:
    version = "bare"

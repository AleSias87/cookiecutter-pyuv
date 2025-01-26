# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import importlib.metadata as metadata

try:
    version = metadata.version("{{cookiecutter.project_slug}}")
except metadata.PackageNotFoundError:
    version = "bare"

project = "{{ cookiecutter.project_name.replace('-', ' ').title() }}"
copyright = "{% now 'local', '%Y' %}, {{cookiecutter.author}}"
author = "{{cookiecutter.author}}"
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.intersphinx",
    {% if cookiecutter.document_api == "y" %}"sphinx.ext.autodoc",
    "sphinx_copybutton",
    {% endif %}]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_persistent": [],
    "secondary_sidebar_items": ["page-toc"],
    "footer_start": ["copyright", "sphinx-version"],
    "footer_end": ["last-updated"],
    "show_nav_level": 2,
    "show_toc_level": 1,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}",
            "icon": "fa-brands fa-github",
        },
    ],
}

html_sidebars = {
    "**": ["search-field", "sidebar-nav-bs"],
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_favicon = ""
html_logo = ""
html_last_updated_fmt = ""
html_css_files = ["custom.css"]

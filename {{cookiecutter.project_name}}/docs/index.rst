{% set project_title = cookiecutter.project_name.replace('-', ' ').title() + " Documentation" %}
.. {{project_title}} documentation master file, created by
   sphinx-quickstart on {% now 'local', '%a %b %d %H:%M:%S %Y' %}.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

{{project_title}}
{{ '=' * project_title | length }}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   {% if cookiecutter.document_api == "y" -%}api{% endif %}

.. toctree::
   :maxdepth: 1
   :caption: Changelog
   :hidden:

   changelog

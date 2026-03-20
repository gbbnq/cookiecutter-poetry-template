# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------
project = "{{cookiecutter.project_slug}}"
copyright = "{{cookiecutter.author}}"
author = "{{cookiecutter.author}}"
release = "{{ cookiecutter.version }}"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "myst_parser",
    "sphinx_rtd_theme",
    {% if cookiecutter.use_notebooks == 'y' -%}
    "nbsphinx",
    {% endif -%}
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "**.ipynb_checkpoints"]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- MyST settings -----------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

# -- Napoleon settings -------------------------------------------------------
napoleon_google_docstring = True
napoleon_include_init_with_doc = True

# -- Autosummary settings ----------------------------------------------------
autosummary_generate = True

# -- Source suffixes ---------------------------------------------------------
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

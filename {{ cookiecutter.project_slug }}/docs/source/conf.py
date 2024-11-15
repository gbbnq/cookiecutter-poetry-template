# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '{{cookiecutter.project_slug}}'
copyright = '{{cookiecutter.author}}'
author = '{{cookiecutter.author}}'
release = '{{ cookiecutter.version }}'

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
    "sphinx.ext.napoleon",
    'sphinx.ext.mathjax',
    'sphinx.ext.autosummary',
    "nbsphinx"
]

templates_path = ['_templates']
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

# Napoleon settings
napoleon_google_docstring = True
napoleon_include_init_with_doc = True

# Autosumamry settings
autosummary_generate = True

# Cookiecutter Template for Python Project

Based on (fpgmaas/cookiecutter-poetry)['https://github.com/fpgmaas/cookiecutter-poetry'] template.

## Usage

- Install [Cookiecutter]('https://github.com/cookiecutter/cookiecutter') package
- Render template using `cookiecutter $PATH_TO_COOKIECUTTER.JSON`
- Enter project details
- Run `make install` to create local .venv and install dependencies
- Run `make test` to run pytests 
- Run `make build` to build project .whl
- Run `make docs-html` to build Sphinx docs
- Run `make publish` to publish python package in artifactory
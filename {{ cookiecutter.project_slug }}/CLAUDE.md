# CLAUDE.md

This file provides guidance for Claude Code when working with this project.

## Project Overview

**{{cookiecutter.project_name}}** - {{cookiecutter.project_description}}

This is a Python data science project managed with [UV](https://docs.astral.sh/uv/) and built with [Hatchling](https://hatch.pypa.io/).

## Build & Run Commands

```bash
make install          # Create venv and install all dependency groups
make check            # Run all checks (lint + type-check + test)
make test             # Run pytest{% if cookiecutter.codecov == "y" %} with coverage{% endif %}
make lint             # Run ruff linter and formatter (with auto-fix)
make lint-check       # Check linting without fixing
make type-check       # Run mypy type checker
make build            # Build wheel
make clean            # Remove build artifacts and caches
{%- if cookiecutter.use_notebooks == "y" %}
make lab              # Launch JupyterLab
{%- endif %}
{%- if cookiecutter.sphinx == "y" %}
make docs             # Build Sphinx HTML documentation
make docs-serve       # Build and serve docs locally
{%- endif %}
```

## Project Structure

```
{{cookiecutter.project_slug}}/
├── {{cookiecutter.project_slug}}/    # Source package
│   └── __init__.py
├── tests/                            # Test files
│   └── conftest.py
├── notebooks/                        # Jupyter notebooks
├── data/                             # Data directory (not committed to git)
│   ├── raw/                          # Original immutable data
│   ├── processed/                    # Cleaned/transformed data
│   └── outputs/                      # Model outputs, figures, reports
├── configs/                          # Configuration files
{%- if cookiecutter.sphinx == "y" %}
├── docs/                             # Sphinx documentation
{%- endif %}
├── pyproject.toml                    # Project metadata and dependencies
├── Makefile                          # Common development commands
└── CLAUDE.md                         # This file
```

## Code Conventions

- **Python version**: >= {{cookiecutter.python_version}}
- **Formatting & linting**: ruff (line length 120)
- **Type checking**: mypy with strict mode
- **Testing**: pytest with tests in `tests/`
- **Imports**: sorted by ruff (isort rules), first-party package is `{{cookiecutter.project_slug}}`
- **Docstrings**: Google style (Napoleon extension for Sphinx)
- **Dependencies**: managed via `uv add` / `uv remove`, groups defined in pyproject.toml

## Key Dependencies

- **Data**: numpy, pandas, polars, pyarrow
- **ML**: scikit-learn
- **Visualization**: matplotlib, seaborn, plotly
- **Config**: pydantic, python-dotenv
- **Logging**: loguru

## Workflow

1. Run `make install` after cloning
2. Use `make check` before committing to ensure all checks pass
3. Add dependencies with `uv add <package>` or `uv add --group dev <package>`
4. Keep notebooks in `notebooks/`, source code in `{{cookiecutter.project_slug}}/`
5. Raw data goes in `data/raw/`, processed data in `data/processed/`

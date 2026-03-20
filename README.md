# Cookiecutter Template: Python Data Science Project

A modern, opinionated Cookiecutter template for Python data science projects. Uses **UV** for fast dependency management, **ruff** for linting/formatting, and comes pre-configured for data science workflows.

## Features

- **UV** for blazing-fast dependency management and virtual environments
- **Hatchling** build backend (PEP 517)
- **Ruff** for linting and formatting (replaces black, isort, flake8)
- **Mypy** for type checking
- **Pytest** with optional coverage
- **Pre-commit** hooks (ruff, nbstripout, trailing whitespace, etc.)
- **JupyterLab** integration
- **Sphinx** documentation with MyST (Markdown) support
- **GitHub Actions** CI/CD
- **DVC** support (optional)
- **CLAUDE.md** for Claude Code integration
- Data science directory structure (`data/raw`, `data/processed`, `data/outputs`)

## Quick Start

```bash
# Install cookiecutter (or use uvx)
pip install cookiecutter

# Render the template
cookiecutter /path/to/this/template

# Or directly from git
cookiecutter gh:your-username/SimplePythonProject
```

## Template Options

| Option | Default | Description |
|---|---|---|
| `project_name` | My Data Science Project | Human-readable project name |
| `project_slug` | (auto-generated) | Python package name |
| `project_description` | A modern Python data science project | Short description |
| `author` | Author Fullname | Your name |
| `email` | author@email.com | Your email |
| `python_version` | 3.12 | Minimum Python version |
| `version` | 0.1.0 | Initial version |
| `use_notebooks` | y | Include JupyterLab and notebook tooling |
| `use_dvc` | n | Include DVC for data versioning |
| `codecov` | y | Include pytest-cov for coverage |
| `sphinx` | y | Include Sphinx documentation |

## After Generation

```bash
cd your_project_slug
make install    # Create venv, install deps, set up pre-commit
make check      # Run lint + type-check + tests
make lab        # Launch JupyterLab
```

## Requirements

- [UV](https://docs.astral.sh/uv/) >= 0.5
- Python >= 3.12 (configurable)

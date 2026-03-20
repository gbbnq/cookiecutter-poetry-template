# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Setup

```bash
make install    # Create venv and install all dependencies
```

## Development

```bash
make check      # Run all checks (lint, type-check, test)
make test       # Run tests
make lint       # Lint and format code
make type-check # Run mypy
{%- if cookiecutter.use_notebooks == "y" %}
make lab        # Launch JupyterLab
{%- endif %}
{%- if cookiecutter.sphinx == "y" %}
make docs       # Build documentation
{%- endif %}
```

## Project Structure

```
├── {{cookiecutter.project_slug}}/    # Source package
├── tests/                            # Tests
├── notebooks/                        # Jupyter notebooks
├── data/
│   ├── raw/                          # Original immutable data
│   ├── processed/                    # Cleaned/transformed data
│   └── outputs/                      # Results, figures, reports
├── configs/                          # Configuration files
{%- if cookiecutter.sphinx == "y" %}
├── docs/                             # Documentation
{%- endif %}
├── pyproject.toml                    # Dependencies and project metadata
├── Makefile                          # Development commands
└── CLAUDE.md                         # Claude Code project guide
```

## Dependencies

Managed with [UV](https://docs.astral.sh/uv/). Add new packages:

```bash
uv add <package>              # Runtime dependency
uv add --group dev <package>  # Development dependency
```

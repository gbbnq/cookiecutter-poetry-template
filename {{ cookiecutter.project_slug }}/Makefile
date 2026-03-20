.PHONY: install
install: ## Install the uv environment and pre-commit hooks
	@echo "🚀 Creating virtual environment using uv"
	@uv sync --all-groups
	@echo "🚀 Installing pre-commit hooks"
	@uv run pre-commit install

.PHONY: check
check: lint type-check test ## Run all checks (lint, type-check, test)

.PHONY: lint
lint: ## Run ruff linter and formatter
	@echo "🚀 Linting code with ruff"
	@uv run ruff check {{cookiecutter.project_slug}} tests --fix
	@uv run ruff format {{cookiecutter.project_slug}} tests

.PHONY: lint-check
lint-check: ## Check linting without fixing
	@uv run ruff check {{cookiecutter.project_slug}} tests
	@uv run ruff format --check {{cookiecutter.project_slug}} tests

.PHONY: type-check
type-check: ## Run mypy type checker
	@echo "🚀 Type checking with mypy"
	@uv run mypy {{cookiecutter.project_slug}}

.PHONY: test
test: ## Run tests with pytest
	@echo "🚀 Running pytest"
{%- if cookiecutter.codecov == "y"%}
	@uv run pytest --cov --cov-config=pyproject.toml --cov-report=xml --cov-report=term-missing
{%- else %}
	@uv run pytest
{%- endif%}

{%- if cookiecutter.use_notebooks == "y" %}

.PHONY: lab
lab: ## Launch JupyterLab
	@echo "🚀 Launching JupyterLab"
	@uv run --group notebooks jupyter lab --notebook-dir=notebooks
{%- endif %}

.PHONY: build
build: clean ## Build wheel file
	@echo "🚀 Building wheel"
	@uv build

.PHONY: clean
clean: ## Clean build artifacts
	@rm -rf dist build *.egg-info .pytest_cache .mypy_cache .ruff_cache .coverage coverage.xml
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

.PHONY: publish
publish: ## Publish package (set UV_PUBLISH_URL, UV_PUBLISH_USERNAME, UV_PUBLISH_PASSWORD)
	@if [ -z "$(UV_PUBLISH_URL)" ]; then \
		echo "❌ Error: UV_PUBLISH_URL not set"; \
		exit 1; \
	fi
	@echo "🚀 Publishing package"
	@uv publish

.PHONY: version-patch
version-patch: ## Bump patch version (1.2.3 => 1.2.4)
	@uv version --bump patch
	@$(MAKE) _sync-version

.PHONY: version-minor
version-minor: ## Bump minor version (1.2.3 => 1.3.0)
	@uv version --bump minor
	@$(MAKE) _sync-version

.PHONY: version-major
version-major: ## Bump major version (1.2.3 => 2.0.0)
	@uv version --bump major
	@$(MAKE) _sync-version

.PHONY: _sync-version
_sync-version:
	@NEW_VERSION=$$(uv version | awk '{print $$2}') && \
	sed -i "s/__version__ = \".*\"/__version__ = \"$$NEW_VERSION\"/" {{cookiecutter.project_slug}}/__init__.py && \
	echo "✅ Version bumped to $$NEW_VERSION"

{%- if cookiecutter.sphinx == "y" %}

.PHONY: docs
docs: ## Build HTML documentation
	@echo "🚀 Building documentation"
	@uv run --group docs sphinx-build -b html docs/source docs/_build/html

.PHONY: docs-serve
docs-serve: docs ## Build and serve documentation locally
	@echo "🚀 Serving docs at http://localhost:8000"
	@cd docs/_build/html && uv run python -m http.server 8000
{%- endif%}

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

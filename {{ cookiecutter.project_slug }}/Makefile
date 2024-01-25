.PHONY: install
install: ## Install the poetry environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install
	@poetry run pre-commit install
	@poetry shell

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
{%- if cookiecutter.codecov == "y"%}
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml
{%- else %}
	@poetry run pytest --doctest-modules
{%- endif%}

.PHONY: build
build: clean-build ## Build wheel file using poetry
	@echo "🚀 Creating wheel file"
	@poetry build

.PHONY: clean-build
clean-build: ## clean build artifacts
	@rm -rf dist

.PHONY: publish
publish: ## Publish to the Artifactory repository using poetry. Requires ARTIFACTORY_TOKEN to be set.
	@echo "🚀 Publishing: Dry run."
	@poetry config repositories.artifactory $(ARTIFACTORY_URL)
	@poetry publish --repository artifactory --username $(ARTIFACTORY_USERNAME) --password $(ARTIFACTORY_PASSWORD) --dry-run
	@echo "🚀 Publishing."
	@poetry publish --repository artifactory --username $(ARTIFACTORY_USERNAME) --password $(ARTIFACTORY_PASSWORD)

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.

{%- if cookiecutter.sphinx == "y" %}

.PHONY: docs-html
docs-html: ## Build and serve the documentation
	@echo "🚀 Building HTML documentation"
	@poetry run sphinx-build -b html docs/source docs/_build/html

{%- endif%}

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
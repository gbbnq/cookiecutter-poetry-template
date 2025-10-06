.PHONY: install
install: ## Install the uv environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using uv"
	@uv venv --clear
	@echo "🚀 Installing dependencies"
	@uv sync --all-groups

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
{%- if cookiecutter.codecov == "y"%}
	@uv run pytest --cov --cov-config=pyproject.toml --cov-report=xml
	@uv run coverage report -m
{%- else %}
	@uv run pytest --doctest-modules
{%- endif%}

.PHONY: build
build: clean ## Build wheel file using uv
	@echo "🚀 Creating wheel file"
	@uv build

.PHONY: clean
clean: ## clean build artifacts
	@rm -rf dist

.PHONY: publish
publish: ## Publish to the Artifactory repository using uv. Requires ARTIFACTORY_TOKEN to be set.
	@if [ -z "$(ARTIFACTORY_URL)" ] || [ -z "$(ARTIFACTORY_USERNAME)" ] || [ -z "$(ARTIFACTORY_PASSWORD)" ]; then \
		echo "❌ Error: Missing environment variables ARTIFACTORY_URL, ARTIFACTORY_USERNAME, or ARTIFACTORY_PASSWORD"; \
		exit 1; \
	fi
	@echo "🚀 Publishing to Artifactory"
	@UV_PUBLISH_URL="$(ARTIFACTORY_URL)" UV_PUBLISH_USERNAME="$(ARTIFACTORY_USERNAME)" UV_PUBLISH_PASSWORD="$(ARTIFACTORY_PASSWORD)" uv publish

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.

.PHONY: version-patch
version-patch: ## Bump patch version (1.2.3 => 1.2.4)
	@echo "🚀 Bumping patch version"
	@uv version --bump patch
	@$(MAKE) _update-init-version
	@$(MAKE) _git-tag-and-push

.PHONY: version-minor
version-minor: ## Bump minor version (1.2.3 => 1.3.0)
	@echo "🚀 Bumping minor version"
	@uv version --bump minor
	@$(MAKE) _update-init-version
	@$(MAKE) _git-tag-and-push

.PHONY: version-major
version-major: ## Bump major version (1.2.3 => 2.0.0)
	@echo "🚀 Bumping major version"
	@uv version --bump major
	@$(MAKE) _update-init-version
	@$(MAKE) _git-tag-and-push

.PHONY: _update-init-version
_update-init-version: ## Internal: Update version in __init__.py
	@echo "🔄 Updating version in __init__.py"
	@NEW_VERSION=$$(uv version | awk '{print $$2}') && \
	sed -i "s/__version__ = \".*\"/__version__ = \"$$NEW_VERSION\"/" {{cookiecutter.project_slug}}/__init__.py && \
	echo "✅ Updated __init__.py to version $$NEW_VERSION"

.PHONY: _git-tag-and-push
_git-tag-and-push: ## Internal: Create git tag and push
	@echo "🏷️ Creating git tag and pushing to remote"
	@NEW_VERSION=$$(uv version | awk '{print $$2}') && \
	git add pyproject.toml {{cookiecutter.project_slug}}/__init__.py && \
	git commit -m "Bump version to $$NEW_VERSION" && \
	git tag "v$$NEW_VERSION" && \
	git push origin main && \
	git push origin "v$$NEW_VERSION" && \
	echo "✅ Tagged and pushed version $$NEW_VERSION"

{%- if cookiecutter.sphinx == "y" %}

.PHONY: docs-html
docs-html: ## Build and serve the documentation
	@echo "🚀 Building HTML documentation"
	@uv run --all-groups sphinx-build -b html docs/source docs/_build/html

{%- endif%}

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

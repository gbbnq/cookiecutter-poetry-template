# Cookiecutter Template for Python Project

This is a simple and customizable Cookiecutter template for starting a new Python project. It leverages Poetry for dependency management and packaging. Based on [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).

## Basic Usage

1. **Install Cookiecutter**: Install the [Cookiecutter](https://github.com/cookiecutter/cookiecutter) package using pip:
    ```sh
    pip install cookiecutter
    ```

2. **Render Template**: Use Cookiecutter to render the template by specifying the path to the `cookiecutter.json` file:
    ```sh
    cookiecutter $PATH_TO_COOKIECUTTER.JSON
    ```

3. **Enter Project Details**: Fill in the required project details in the `cookiecutter.json` file:
    - `project_name`: The name of your project.
    - `project_slug`: The project slug, automatically generated from the project name.
    - `project_description`: A short description of your project.
    - `author`: The full name of the author.
    - `email`: The email address of the author.
    - `python_version`: The version of Python to use.
    - `version`: The initial version of the project.
    - `use_pytest`: Whether to include pytest for testing (y/n).
    - `codecov`: Whether to include Codecov for code coverage (y/n).
    - `sphinx`: Whether to include Sphinx for documentation (y/n).
    - `bayer_int`: 'y' if Bayer internal workflow for documentation deployment is to be used. Is 'n' by default.

4. **Install Dependencies**: Create a local virtual environment and install dependencies using Poetry:
    ```sh
    make install
    ```

5. **Run Tests**: Execute tests using pytest:
    ```sh
    make test
    ```

6. **Build Project**: Build the project into a .whl file:
    ```sh
    make build
    ```

7. **Build Documentation**: Generate HTML documentation using Sphinx:
    ```sh
    make docs-html
    ```

8. **Publish Package**: Publish the Python package to Artifactory:
    ```sh
    make publish
    ```

## Additional Information

- **Poetry**: Poetry is used for dependency management and packaging. Ensure you have Poetry installed. For installation instructions, visit the [Poetry documentation](https://python-poetry.org/docs/#installation).
- **Cookiecutter**: Cookiecutter is a command-line utility that creates projects from project templates. For more information, visit the [Cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/).
- **Makefile**: The provided `Makefile` includes various commands to streamline your workflow. Use `make <command>` to execute the corresponding tasks.

"""Tests for {{cookiecutter.project_slug}}."""

from {{cookiecutter.project_slug}} import __version__


def test_version():
    """Test version is set."""
    assert __version__ == "{{ cookiecutter.version }}"

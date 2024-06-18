"""
This module contains tests for the `pep` package.

It uses the `pytest` framework to test various functions and classes of the package.
"""

from pep import version


def test_loading_project():
    """
    Test loading the project
    """

    print(f"The installed version is {version.__version__}")

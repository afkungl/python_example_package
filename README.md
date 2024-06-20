# Example package for projects in Python
A basic python package with sensible structure, logging, testing and documentation.

[![Build and test](https://github.com/afkungl/python_example_package/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/afkungl/python_example_package/actions/workflows/python-app.yml)
[![Linting](https://github.com/afkungl/python_example_package/actions/workflows/linting.yml/badge.svg?branch=main)](https://github.com/afkungl/python_example_package/actions/workflows/linting.yml)
[![Stylecheck](https://github.com/afkungl/python_example_package/actions/workflows/stylecheck.yml/badge.svg?branch=main)](https://github.com/afkungl/python_example_package/actions/workflows/stylecheck.yml)

# Getting Started

## Installation
Create a new anaconda environment as specified in the environment file and activate it:
````bash
conda env create -f environment.yaml
conda activate 240606_proj_example
````
This environment contains packages that are required for development but not necessary for usage.
Install the package via pip:
````bash
pip install .
````
Verify the installation by running the tests.
````bash
pytest tests
````

# Documentation
Creating the documentation requires the sphinx python package.
It is installed via the _environment.yaml_.
For installation navigate to the docs folder and run:
````bash
sphinx-build -M html . _build
````
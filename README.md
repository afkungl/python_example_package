# Example package for projects in Python
A basic python package with sensible structure, logging, testing and documentation.

[![Build and test](https://github.com/afkungl/python_example_package/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/afkungl/python_example_package/actions/workflows/python-app.yml)
[![Linting](https://github.com/afkungl/python_example_package/actions/workflows/linting.yml/badge.svg?branch=main)](https://github.com/afkungl/python_example_package/actions/workflows/linting.yml)
[![Stylecheck](https://github.com/afkungl/python_example_package/actions/workflows/stylecheck.yml/badge.svg?branch=main)](https://github.com/afkungl/python_example_package/actions/workflows/stylecheck.yml)

# Getting Started

The project is meant to be a starting point for new projects in Python.
It features:
- A basic package structure
- setup.py for installation
- Logging: Both app-level logging with config and library-style logging
- Testing with pytest
- Codestyle and linting with configuration files
- Documentation with sphinx
- Github Actions for CI/CD
- Anaconda environment file for development

# Usage

To start a new project, first copy/fork/import this repository to an own one.
Then start with the customization:
- fill up src with your own code
- you can use the src/applogger.py as is or modify it
- add your own tests to the tests folder
- modify the setup.py to your needs, i.e. change the package name
- modify the environment.yaml to your needs
- modify the .github/workflows files to your needs. Adapt them to other systems if necessary
- Change the LICENCE for the new project. This project uses the permissive MIT licence

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
# Example package for projects in Python
A basic python package with sensible structure, logging, testing and documentation.


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
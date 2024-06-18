import os
from setuptools import setup, find_packages
from distutils.util import convert_path

# get the version from sourcecode
main_ns = {}
ver_path = convert_path('src/pep/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

ci_version = os.environ.get('BUILD_BUILDNUMBER', main_ns['__version__'])


setup(
    name='python_example_package',
    version=ci_version,
    packages=find_packages() + [
        "pep",
        "pep.games"
    ],
    package_dir={"pep": "src/pep",
                 "pep.games": "src/pep/games"},
    author='Akos F Kungl',
    description='Example Package to start other packages from',
    url='https://github.com/afkungl/python_example_package',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'numpy==1.26.4',
        'pytest'
    ]
)

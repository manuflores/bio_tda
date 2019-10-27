import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='tda',
    version='0.0.1',
    author='Emanuel Flores B., Jorge Flores, Andres Ortiz',
    author_email='efflores@caltech.edu',
    description='Utilities for making topological data analysis in python.',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='bio_tda',
    version='0.0.1',
    author='Emanuel Flores B., Jorge A. Flores, Andres Ortiz',
    author_email='manuflores@caltech.edu',
    description='Utilities for TDA bindings in Python.',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)

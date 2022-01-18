from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup_args = {
    "name": "precommit_nbconvert_rename",
    "version": "1.0",
    "packages": find_packages(),
    "install_requires": [
        "jupyter-client>=7.1.1",  # BSD-3 https://github.com/jupyter/jupyter_client/blob/main/COPYING.md
        "nbconvert>=6.4.0",  # BSD-3 https://github.com/jupyter/nbconvert/blob/main/LICENSE
        "pre-commit>=2.16.0",  # MIT https://github.com/pre-commit/pre-commit/blob/master/LICENSE
        "typer>=0.4.0",  # MIT https://github.com/tiangolo/typer/blob/master/LICENSE
    ],
    "author": "Tim Vink",
    "author_email": "tim.vink@allianzdirect.nl",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/allianz-direct/precommit_nbconvert_rename",
    "keywords": "precommit nbconvert nbstripout jupyter notebook python",
    "license": "MIT",
    "python_requires": ">=3.7",
    "classifiers": [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    "entry_points": {
        "console_scripts": [
            "nb_convert_strip=precommit_nbconvert_rename.cli:app",
        ]
    },
}

setup(**setup_args)

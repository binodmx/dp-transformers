# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os
from setuptools import setup, find_packages

version = '1.0.1'

with open('README.md') as f:
    long_description = f.read()

setup(
    name='dp-transformers',
    version=version,
    description='Differentially-private transformers using HuggingFace and Opacus',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://www.github.com/microsoft/dp-transformers",
    author='Microsoft',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires=">=3.7.0",
    include_package_data=True,
    extras_require={
        "test": [
            "pytest",
        ]
    },
    install_requires=[
        "transformers>=4.30.0",
        "datasets>=2.0.0",
        "opacus>=1.5.4",
        "peft",
        "prv_accountant<0.2.0",
        "torch>=2.6.0",
    ],
    test_suite="tests",
    zip_safe=False
)

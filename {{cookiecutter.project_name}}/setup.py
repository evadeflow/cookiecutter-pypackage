#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages

readme = open('README.md').read()

# See: https://pypi.python.org/pypi/pytest-runner#conditional-requirement
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(
    author='Blue Newt Software',
    author_email='support@blue-newt.com',
    classifiers=[
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    description='{{ cookiecutter.project_short_description }}',
    include_package_data=True,
    install_requires=[
        # TODO: Add requirements here
    ],
    keywords='{{ cookiecutter.package_name }}',
    long_description=readme,
    name='{{ cookiecutter.package_name }}',
    namespace_packages=['{{ cookiecutter.package_name.split(".")[0] }}' ],
    packages=find_packages(),
    setup_requires=[
        'setuptools_scm',
    ] + pytest_runner,
    test_suite='tests',
    tests_require=[
        'coverage',
        'pytest',
    ],
    use_scm_version={
        'root': '..',
        'version_scheme': 'post-release',
    },
    zip_safe=False,
)

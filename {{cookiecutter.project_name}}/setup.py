#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup, find_packages

readme = open('README.md').read()

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
    license="BSD",
    long_description=readme,
    name='{{ cookiecutter.package_name }}',
    namespace_packages=['{{ cookiecutter.package_name.split(".")[0] }}' ],
    packages=find_packages(),
    setup_requires=[
        'pytest-runner',
        'setuptools_scm'
    ],
    test_suite='tests',
    tests_require=[
        'coverage',
        'pytest',
    ],
    url='{{ cookiecutter.vcs_url }}',
    use_scm_version=True,
    zip_safe=False,
)

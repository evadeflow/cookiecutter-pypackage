#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup, find_packages

readme = open('README.md').read()

# NB: _don't_ add namespace_packages to setup(), it'll break
#     everything using imp.find_module
setup(
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
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
    packages=[
        '{{ cookiecutter.package_name }}',
    ],
    setup_requires=['setuptools_scm'],
    test_suite='tests',
    url='{{ cookiecutter.vcs_url }}',
    use_scm_version=True,
    zip_safe=False,
)

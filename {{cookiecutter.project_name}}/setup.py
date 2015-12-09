#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages

readme = open('README.md').read()

# Skip pytest-runner install if not testing, see:
#   https://pypi.python.org/pypi/pytest-runner#conditional-requirement
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner>=2.0,<3dev'] if needs_pytest else []

# Temp hack to work around the lack of an SCM working copy in our current
# deploys: just return a hard-coded, dummy value if the lookup via SCM tags
# would fail.
def _get_version(*args, **kwds):

    for scm_path in ('.', '..'):
        try:
            from setuptools_scm import get_version
            return get_version(root=scm_path, version_scheme='post-release')
        except:
            pass

    return '0.1.0'

namespace_packages = (
    ['{{ cookiecutter.package_name.split(".")[0] }}']
    if '.' in '{{ cookiecutter.package_name }}'
    else []
)

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
    namespace_packages=namespace_packages,
    packages=find_packages(),
    setup_requires=[
        'setuptools_scm>=1.10.0',
    ] + pytest_runner,
    test_suite='tests',
    tests_require=[
        'coverage',
        'pytest',
    ],
    use_scm_version=dict(parse=_get_version),
    zip_safe=False,
)

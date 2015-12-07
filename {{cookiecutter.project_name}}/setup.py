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
dummy_version = '0.1.0'
class GetUseScmVersionArg():

    def dummy_version_from_scm(self, scm_root):
        return dummy_version

    def __call__(self, *args, **kwds):
        import setuptools_scm

        scm_version_okay = False
        for scm_path in ('.', '..'):
            try:
                setuptools_scm.get_version(scm_path)
                scm_version_okay = True
                break
            except LookupError:
                pass

        if not scm_version_okay:
            # Monkey patch the internal setuptools_scm function version_from_scm()
            setattr(setuptools_scm, 'version_from_scm', self.dummy_version_from_scm)

        return { 'root': scm_path, 'version_scheme': 'post-release' }

    def pop(self, value, retval=None):
        return retval

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
    use_scm_version=GetUseScmVersionArg(),
    version=dummy_version,
    zip_safe=False,
)

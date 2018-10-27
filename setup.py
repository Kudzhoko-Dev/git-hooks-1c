# -*- coding: utf-8 -*-
from __future__ import absolute_import

from setuptools import find_packages, setup

import git_hooks_1c

setup(
    name='git_hooks_1c',
    version=git_hooks_1c.__version__,
    description='Git hooks utilities for 1C:Enterprise',
    author='Cujoko',
    author_email='cujoko@gmail.com',
    url='https://gitlab.com/Cujoko/git-hooks-1c',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    keywords='1c git pre-commit v8reader v8unpack gcomp',
    package_data={
        'git_hooks_1c': [
            'pre-commit-1c.bat',
            'pre-commit.sample'
        ]
    },
    entry_points={
        'console_scripts': [
            'gh1c=git_hooks_1c.__main__:run'
        ]
    },
    license='MIT',
    install_requires=[
        'commons @ https://gitlab.com/Cujoko/commons/-/archive/master/commons-master.tar.gz#egg=commons-2.1.0',
        'parse-1c-build @ https://gitlab.com/Cujoko/parse-1c-build/-/archive/master/parse-1c-build-master.tar.gz'
        '#egg=parse_1c_build-4.3.0'
    ]
)

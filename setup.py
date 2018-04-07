# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

import git_hooks_1c

setup(
    name='git_hooks_1c',
    version=git_hooks_1c.__version__,
    description='Git hooks utilities for 1C:Enterprise',
    author='Cujoko',
    author_email='cujoko@gmail.com',
    url='https://github.com/Cujoko/git-hooks-1c',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    keywords='1c git pre-commit v8reader v8unpack gcomp',
    package_data={
        'git_hooks_1c': [
            'pre-commit.sample',
            'pre-commit-1c.bat'
        ]
    },
    entry_points={
        'console_scripts': [
            'gh1c=git_hooks_1c.__main__:run'
        ]
    },
    license = 'MIT'
)

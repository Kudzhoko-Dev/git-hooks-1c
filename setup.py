#! python3
# -*- coding: utf-8 -*-
import githooks1c
from setuptools import setup, find_packages


setup(
    name='githooks1c',
    version=githooks1c.__version__,
    url='https://github.com/Cujoko/githooks1c',

    author='Cujoko',
    author_email='cujoko@gmail.com',

    install_requires=[
        'decompiler1cwrapper'
    ],

    packages=find_packages(),
    package_data={
        'githooks1c': [
            'pre-commit.sample',
            'pre-commit-1c.bat'
        ]
    },

    entry_points={
        'console_scripts': [
            'clihp=githooks1c.createlinksinhooks:create_links_in_hooks_pre_commit',
            'precommit1c=githooks1c.precommit1c:main'
        ]
    }
)

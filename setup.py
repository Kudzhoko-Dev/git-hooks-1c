#! python3
# -*- coding: utf-8 -*-
import githooksfor1c
from setuptools import setup, find_packages


setup(
    name='githooksfor1c',
    version=githooksfor1c.__version__,
    url='https://github.com/Cujoko/githooksfor1c',

    author='Cujoko',
    author_email='cujoko@gmail.com',

    install_requires=[
        'decompiler1cwrapper'
    ],

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'precommit1c=githooksfor1c.precommit1c:main'
        ]
    }
)

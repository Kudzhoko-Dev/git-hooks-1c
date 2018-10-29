# -*- coding: utf-8 -*-
from __future__ import absolute_import

import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with codecs.open(os.path.join(here, 'git_hooks_1c', '__about__.py'), 'r', 'utf-8') as f:
    exec (f.read(), about)

setup(
    name='git_hooks_1c',
    version=about['__version__'],
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
        'commons @ https://gitlab.com/Cujoko/commons/-/archive/master/commons-master.tar.gz',
        'parse-1c-build @ https://gitlab.com/Cujoko/parse-1c-build/-/archive/master/parse-1c-build-master.tar.gz'
    ]
)

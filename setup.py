# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import setup

here = Path(__file__).parent

about = {}
with Path(here, 'git_hooks_1c', '__about__.py').open() as f:
    exec(f.read(), about)

setup(
    name='git-hooks-1c',
    version=about['__version__'],
    description='Git hooks utilities for 1C:Enterprise',
    author='Cujoko',
    author_email='cujoko@gmail.com',
    url='https://github.com/Cujoko/git-hooks-1c',
    packages=['git_hooks_1c'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    keywords='1c git pre-commit v8reader v8unpack gcomp',
    package_data={
        'git_hooks_1c': [
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
        'cjk-commons>=3.3.0',
        'parse-1c-build>=5.5.0'
    ]
)

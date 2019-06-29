# -*- coding: utf-8 -*-
from pathlib import Path
import subprocess
import sys

from loguru import logger


# noinspection PyUnusedLocal
def run(args) -> None:
    try:
        hooks_dir_fullpath = Path('.git', 'hooks').absolute()
        if not hooks_dir_fullpath.is_dir():
            logger.error('not a git repo')
            return

        pre_commit_file_fullpath = Path(hooks_dir_fullpath, 'pre-commit')
        if pre_commit_file_fullpath.exists() and not args.force:
            logger.info('git-hooks-1c already exist')
            return

        with pre_commit_file_fullpath.open('w') as pre_commit_file:
            pre_commit_file.write('#!/bin/sh\n')
            pre_commit_file.write('cmd //C "gh1c.exe pre_commit{}"\n'.format(
                ' -s' if args.only_source_files else ''))  # todo

        subprocess.call(['cmd.exe', '/C', 'git', 'config', '--local', 'core.quotepath', 'false'])
        subprocess.call(['cmd.exe', '/C', 'git', 'config', '--local', 'core.longpaths', 'true'])
        logger.info('git-hooks-1c installed')

    except Exception as e:
        logger.exception(e)
        sys.exit(1)


def add_subparser(subparsers) -> None:
    decs = 'Install hooks'
    subparser = subparsers.add_parser(
        Path(__file__).stem,
        help=decs,
        description=decs,
        add_help=False
    )
    subparser.set_defaults(func=run)
    subparser.add_argument(
        '-h', '--help',
        action='help',
        help='Show this help message and exit'
    )
    subparser.add_argument(
        '-f', '--force',
        action='store_true',
        help='Install hooks anyway'
    )
    subparser.add_argument(
        '-s', '--only-source-files',
        action='store_true',
        help='Remove 1C-files from index (add to index source files only)'
    )

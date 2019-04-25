# -*- coding: utf-8 -*-
import logging
from pathlib import Path
import subprocess

import shutil

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def run(args) -> None:
    try:
        script_dir_fullpath = Path(__file__).parent.absolute()
        hooks_dir_fullpath = Path('.git', 'hooks').absolute()
        pre_commit_file_fullpath = Path(hooks_dir_fullpath, 'pre-commit')
        if pre_commit_file_fullpath.exists() and not args.force:
            print('git-hooks-1c already exist')
        else:
            with pre_commit_file_fullpath.open('w') as pre_commit_file:
                pre_commit_file.write('#!/bin/sh\n')
                pre_commit_file.write('cmd //C "gh1c.exe pre_commit{}"\n'.format(
                    ' -s' if args.only_source_files else ''))  # todo
            print('git-hooks-1c installed')
        subprocess.call(['cmd.exe', '/C', 'git', 'config', '--local', 'core.quotepath', 'false'])
        subprocess.call(['cmd.exe', '/C', 'git', 'config', '--local', 'core.longpaths', 'true'])
    except Exception as e:
        logger.exception(e)


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

# -*- coding: utf-8 -*-
import sys
from pathlib import Path

from loguru import logger
from plumbum import local

logger.disable(__name__)


def run(args) -> None:
    logger.enable('cjk_commons')
    logger.enable('parse_1c_build')
    logger.enable(__name__)

    hooks_dir_fullpath = Path('.git', 'hooks').absolute()
    if not hooks_dir_fullpath.is_dir():
        logger.error('not a git repo')
        return
        
    pre_commit_file_fullpath = Path(hooks_dir_fullpath, 'pre-commit')
    if pre_commit_file_fullpath.exists() and not args.force:
        logger.info('git-hooks-1c already exist')
        return

    try:
        with pre_commit_file_fullpath.open('w') as pre_commit_file:
            pre_commit_file.write('#!/bin/sh\n')
            pre_commit_file.write(f'gh1c pre-commit{" -a" if args.keep_files else ""}\n')

        git = local['git']
        git('config', '--local', 'core.quotepath', 'false')
        git('config', '--local', 'core.longpaths', 'true')

        logger.info('git-hooks-1c installed')
    except Exception as e:
        logger.exception(e)
        sys.exit(1)


def add_subparser(subparsers) -> None:
    decs = 'Install hooks'
    subparser = subparsers.add_parser(
        Path(__file__).stem.replace('_', '-'),
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
        '-k', '--keep-files',
        action='store_true',
        help='Keep 1C-files in the index'
    )

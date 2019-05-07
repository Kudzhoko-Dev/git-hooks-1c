# -*- coding: utf-8 -*-
import logging
from pathlib import Path
import sys

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def run(args) -> None:
    try:
        hooks_dir_fullpath = Path('.git', 'hooks').absolute()
        if not hooks_dir_fullpath.is_dir():
            logger.error('not a git repo')
            return

        pre_commit_file_fullpath = Path(hooks_dir_fullpath, 'pre-commit')
        if not pre_commit_file_fullpath.exists():
            logger.info('git-hooks-1c not installed')
            return

        pre_commit_file_fullpath.unlink()
        logger.info('git-hooks-1c uninstalled')

    except Exception as e:
        logger.exception(e)
        sys.exit(1)


def add_subparser(subparsers) -> None:
    decs = 'Uninstall hooks'
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

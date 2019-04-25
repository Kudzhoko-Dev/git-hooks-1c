# -*- coding: utf-8 -*-
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def run(args) -> None:
    try:
        hooks_dir_fullpath = Path('.git', 'hooks').absolute()
        pre_commit_file_fullpath = Path(hooks_dir_fullpath, 'pre-commit')
        if pre_commit_file_fullpath.exists():
            pre_commit_file_fullpath.unlink()
            print('git-hooks-1c uninstalled')
        else:
            print('git-hooks-1c not installed')
    except Exception as e:
        logger.exception(e)


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

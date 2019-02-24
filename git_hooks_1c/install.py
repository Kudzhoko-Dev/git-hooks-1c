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
        current_dir_fullpath = Path('.git', 'hooks').absolute()
        pre_commit_file_fullpath = Path(script_dir_fullpath, 'pre-commit.sample')
        pre_commit_symbolic_fullpath = Path(current_dir_fullpath, 'pre-commit')
        if pre_commit_symbolic_fullpath.exists() and not args.force:
            print('git-hooks-1c already exist')
        else:
            shutil.copyfile(str(pre_commit_file_fullpath), str(pre_commit_symbolic_fullpath))
            print('git-hooks-1c installed')

        args_au = [
            'cmd.exe',
            '/C',
            'git',
            'config',
            '--local',
            'core.quotepath',
            'false'
        ]
        subprocess.call(args_au)
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

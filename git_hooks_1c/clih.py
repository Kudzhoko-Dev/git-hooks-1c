# -*- coding: utf-8 -*-
import logging
from pathlib import Path
import subprocess

logger: logging.Logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def run(args) -> None:
    try:
        script_dir_fullpath = Path(__file__).parent.absolute()
        current_dir_fullpath = Path('.git', 'hooks').absolute()
        pre_commit_file_fullpath = Path(script_dir_fullpath, 'pre-commit.sample')
        pre_commit_symbolic_fullpath = Path(current_dir_fullpath, 'pre-commit')
        if pre_commit_symbolic_fullpath.exists() or pre_commit_symbolic_fullpath.is_symlink():
            pre_commit_symbolic_fullpath.unlink()
        args_au = [
            'cmd.exe',
            '/C',
            'mklink',
            str(pre_commit_symbolic_fullpath),
            str(pre_commit_file_fullpath)
        ]
        subprocess.call(args_au)
        bat_file_fullpath = Path(script_dir_fullpath, 'pre-commit-1c.bat')
        bat_symbolic_fullpath = Path(current_dir_fullpath, 'pre-commit-1c.bat')
        if bat_symbolic_fullpath.exists() or bat_symbolic_fullpath.is_symlink():
            bat_symbolic_fullpath.unlink()
        args_au = [
            'cmd.exe',
            '/C',
            'mklink',
            str(bat_symbolic_fullpath),
            str(bat_file_fullpath)
        ]
        subprocess.call(args_au)
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
    decs = 'Create links in hooks dir'
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

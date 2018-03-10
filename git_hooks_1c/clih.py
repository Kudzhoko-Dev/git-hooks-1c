# -*- coding: utf-8 -*-
from pathlib import Path
import subprocess
from typing import Any


def run() -> None:
    script_dir_path = Path(__file__).parent
    current_dir_path = Path.cwd() / '.git' / 'hooks'

    pre_commit_file_path = script_dir_path / 'pre-commit.sample'
    pre_commit_symbolic_path = current_dir_path / 'pre-commit'

    if pre_commit_symbolic_path.exists() or pre_commit_symbolic_path.is_symlink():
        pre_commit_symbolic_path.unlink()

    subprocess.call([
        'cmd.exe',
        '/C',
        'mklink',
        str(pre_commit_symbolic_path),
        str(pre_commit_file_path)
    ])

    bat_file_path = script_dir_path / 'pre-commit-1c.bat'
    bat_symbolic_path = current_dir_path / 'pre-commit-1c.bat'

    if bat_symbolic_path.exists() or bat_symbolic_path.is_symlink():
        bat_symbolic_path.unlink()

    subprocess.call([
        'cmd.exe',
        '/C',
        'mklink',
        str(bat_symbolic_path),
        str(bat_file_path)
    ])

    subprocess.call([
        'cmd.exe',
        '/C',
        'git',
        'config',
        '--local',
        'core.quotepath',
        'false'
    ])


def add_subparser(subparsers: Any) -> None:
    decs = 'Create links in hooks dir'
    subparser = subparsers.add_parser(
        Path(__file__).stem,
        help=decs,
        description=decs,
        add_help=False)

    subparser.set_defaults(func=run)

    subparser.add_argument(
        '-h', '--help',
        action='help',
        help='Show this help message and exit')

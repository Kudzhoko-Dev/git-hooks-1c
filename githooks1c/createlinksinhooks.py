#! python3
# -*- coding: utf-8 -*-
from pathlib import Path
import subprocess


def create_links_in_hooks_pre_commit():
    script_dir_path = Path(__file__).parent
    current_dir_path = Path.cwd() / Path('.git', 'hooks')

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


if __name__ == '__main__':
    create_links_in_hooks_pre_commit()

#! python3
# -*- coding: utf-8 -*-
from pathlib import Path
import subprocess


def create_links_in_hooks_pre_commit():
    subprocess.call([
        'cmd.exe',
        '/C',
        'mklink',
        '.git\\hooks\\pre-commit',
        str(Path(__file__).parent / 'pre-commit.sample')
    ])

    subprocess.call([
        'cmd.exe',
        '/C',
        'mklink',
        '.git\\hooks\\pre-commit-1c.bat',
        str(Path(__file__).parent / 'pre-commit-1c.bat')
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

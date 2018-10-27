# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import subprocess

from commons.compat import s, u


# noinspection PyUnusedLocal
def run(args):
    script_dir_fullname = os.path.abspath(os.path.join(u(__file__, 'cp1251'), os.pardir))
    current_dir_fullname = os.path.abspath(os.path.join('.git', 'hooks'))
    pre_commit_file_fullname = os.path.join(script_dir_fullname, 'pre-commit.sample')
    pre_commit_symbolic_fullname = os.path.join(current_dir_fullname, 'pre-commit')
    # todo Возможно, islink не подходит
    if os.path.exists(pre_commit_symbolic_fullname) or os.path.islink(pre_commit_symbolic_fullname):
        os.remove(pre_commit_symbolic_fullname)
    args_au = [
        'cmd.exe',
        '/C',
        'mklink',
        pre_commit_symbolic_fullname,
        pre_commit_file_fullname
    ]
    subprocess.call(s(args_au, 'cp1251'))
    bat_file_fullname = os.path.join(script_dir_fullname, 'pre-commit-1c.bat')
    bat_symbolic_fullname = os.path.join(current_dir_fullname, 'pre-commit-1c.bat')
    # todo Возможно, islink не подходит
    if os.path.exists(bat_symbolic_fullname) or os.path.islink(bat_symbolic_fullname):
        os.remove(bat_symbolic_fullname)
    args_au = [
        'cmd.exe',
        '/C',
        'mklink',
        bat_symbolic_fullname,
        bat_file_fullname
    ]
    subprocess.call(s(args_au, 'cp1251'))
    args_au = [
        'cmd.exe',
        '/C',
        'git',
        'config',
        '--local',
        'core.quotepath',
        'false'
    ]
    subprocess.call(s(args_au, 'cp1251'))


def add_subparser(subparsers):
    decs = 'Create links in hooks dir'
    subparser = subparsers.add_parser(
        os.path.splitext(os.path.basename(__file__))[0],
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

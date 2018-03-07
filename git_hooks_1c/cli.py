# -*- coding: utf-8 -*-
from argparse import ArgumentParser

from git_hooks_1c import __version__, clih, pre_commit


def get_argparser() -> ArgumentParser:
    parser = ArgumentParser(prog='u1c', description='Git hooks utilities for 1C:Enterprise', add_help=False)

    parser.add_argument(
        '-h', '--help',
        action='help',
        help='Show this help message and exit')

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s, ver. {}'.format(__version__),
        help='Show version')

    subparsers = parser.add_subparsers(dest='subparser_name')

    clih.add_subparser(subparsers)
    pre_commit.add_subparser(subparsers)

    return parser

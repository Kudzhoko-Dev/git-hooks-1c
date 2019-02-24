# -*- coding: utf-8 -*-
from argparse import ArgumentParser

from commons.logging_ import add_logging_arguments
from git_hooks_1c import __version__, install, pre_commit, uninstall


def get_argparser() -> ArgumentParser:
    parser = ArgumentParser(
        prog='gh1c', description='Git hooks utilities for 1C:Enterprise', add_help=False)
    parser.add_argument(
        '-h', '--help',
        action='help',
        help='Show this help message and exit'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s, ver. {0}'.format(__version__),
        help='Show version'
    )
    add_logging_arguments(parser)
    subparsers = parser.add_subparsers(dest='subparser_name')
    install.add_subparser(subparsers)
    pre_commit.add_subparser(subparsers)
    uninstall.add_subparser(subparsers)
    return parser

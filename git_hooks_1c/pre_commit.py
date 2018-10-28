# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import shutil
import subprocess

import re

from commons.compat import s
from parse_1c_build import Parser

added_or_modified = re.compile(r'^\s*[AM]\s+"?(?P<rel_name>[^"]*)"?')


def get_added_or_modified_file_fullnames():
    result = []
    try:
        args_au = [
            'git',
            'status',
            '--porcelain'
        ]
        output = subprocess.check_output(s(args_au, 'cp1251')).decode('utf-8')
    except subprocess.CalledProcessError:
        return result
    for line in output.split('\n'):
        if line != '':
            match = added_or_modified.match(line)
            if match:
                added_or_modified_file_fullname = os.path.abspath(match.group('rel_name'))
                if os.path.basename(added_or_modified_file_fullname).lower() != 'readme.md':
                    result.append(added_or_modified_file_fullname)
    return result


def get_for_processing_file_fullnames(file_fullnames):
    result = []
    for file_fullname in file_fullnames:
        if os.path.splitext(file_fullname)[1].lower() in ['.epf', '.erf', '.ert', '.md']:
            result.append(file_fullname)
    return result


def parse(file_fullnames):
    result = []
    parser = Parser()
    for file_fullname in file_fullnames:
        source_dir_fullname = os.path.join(
            os.path.abspath(os.path.join(file_fullname, os.pardir)),
            os.path.splitext(file_fullname)[0] + '_' + os.path.splitext(file_fullname)[1][1:] + '_src')
        if not os.path.exists(source_dir_fullname):
            # fixme Добавить parents=True
            os.mkdir(source_dir_fullname)
        else:
            # todo Было 'ignore_errors=True'. Убрал
            shutil.rmtree(source_dir_fullname)
        parser.run(file_fullname, source_dir_fullname)
        result.append(source_dir_fullname)
    return result


def add_to_index(dir_fullnames):
    for dir_fullname in dir_fullnames:
        args_au = [
            'git',
            'add',
            '--all',
            dir_fullname
        ]
        exit_code = subprocess.check_call(s(args_au, 'cp1251'))
        if exit_code != 0:
            exit(exit_code)


# noinspection PyUnusedLocal
def run(args):
    added_or_modified_file_fullnames = get_added_or_modified_file_fullnames()
    for_processing_file_fullnames = get_for_processing_file_fullnames(added_or_modified_file_fullnames)
    if len(for_processing_file_fullnames) == 0:
        exit(0)
    for_indexing_source_dir_fullnames = parse(for_processing_file_fullnames)
    add_to_index(for_indexing_source_dir_fullnames)


def add_subparser(subparsers):
    decs = 'Pre-commit for 1C:Enterprise files'
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

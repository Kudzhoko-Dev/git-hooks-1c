# -*- coding: utf-8 -*-
from pathlib import Path
import subprocess

import re
import shutil

from parse_1c_build.parse import Parser

added_or_modified = re.compile(r'^\s*[AM]\s+"?(?P<rel_name>[^"]*)"?')


def get_added_or_modified_file_paths():
    result = []
    try:
        output = subprocess.check_output(['git', 'status', '--porcelain']).decode()
    except subprocess.CalledProcessError:
        return result
    for line in output.split('\n'):
        if line != '':
            match = added_or_modified.match(line)
            if match:
                added_or_modified_file_path = Path.cwd() / match.group('rel_name')
                if added_or_modified_file_path.name.lower() != 'readme.md':
                    result.append(added_or_modified_file_path)
    return result


def get_for_processing_file_paths(file_paths):
    result = []
    for file_path in file_paths:
        if file_path.suffix.lower() in ['.epf', '.erf', '.ert', '.md']:
            result.append(file_path)
    return result


def parse(file_paths):
    result = []
    parser = Parser()
    for file_path in file_paths:
        source_dir_path = file_path.parent / (file_path.stem + '_' + file_path.suffix[1:] + '_src')
        if not source_dir_path.exists():
            source_dir_path.mkdir(parents=True)
        else:
            shutil.rmtree(str(source_dir_path), ignore_errors=True)
        parser.run(file_path, source_dir_path)
        result.append(source_dir_path)
    return result


def add_to_index(dir_paths):
    for dir_path in dir_paths:
        exit_code = subprocess.check_call(['git', 'add', '--all', str(dir_path)])
        if exit_code != 0:
            exit(exit_code)


def run():
    added_or_modified_file_paths = get_added_or_modified_file_paths()
    for_processing_file_paths = get_for_processing_file_paths(added_or_modified_file_paths)
    if len(for_processing_file_paths) == 0:
        exit(0)
    for_indexing_source_dir_paths = parse(for_processing_file_paths)
    add_to_index(for_indexing_source_dir_paths)


def add_subparser(subparsers):
    decs = 'Pre-commit for 1C:Enterprise files'
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

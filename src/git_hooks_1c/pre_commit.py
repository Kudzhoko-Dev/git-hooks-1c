# -*- coding: utf-8 -*-
import re
import shutil
import sys
from pathlib import Path

import fleep
from loguru import logger
from parse_1c_build import Parser
from plumbum import local

indexed_pattern = re.compile(r'^\s*[AM]\s+"?(?P<rel_name>[^"]*)"?')
bin_file_suffixes = ['.epf', '.erf', '.ert', '.md']
bin_file_to_check_suffixes = ['.md']

logger.disable(__name__)


def get_indexed_file_fullpaths() -> list[Path]:
    result = []
    git = local['git']
    try:
        output = git('diff-index', '--ignore-submodules', '--name-status', '--cached', 'HEAD')
    except:
        output = git('status', '--ignore-submodules', '--porcelain')
    for line in output.split('\n'):
        if line != '':
            match = indexed_pattern.match(line)
            if match:
                indexed_file_fullpath = Path(match.group('rel_name')).absolute()
                result.append(indexed_file_fullpath)
    return result


def get_for_processing_file_fullpaths(file_fullpaths: list[Path]) -> list[Path]:
    result = []
    for file_fullpath in file_fullpaths:
        if file_fullpath.suffix.lower() in bin_file_suffixes:
            if file_fullpath.suffix.lower() in bin_file_to_check_suffixes:
                with file_fullpath.open('rb') as file:
                    info = fleep.get(file.read(128))
                if info.type == ['document']:
                    result.append(file_fullpath)
            else:
                result.append(file_fullpath)
    return result


def parse(file_fullpaths: list[Path]) -> list[Path]:
    result = []
    parser = Parser()
    for file_fullpath in file_fullpaths:
        source_dir_fullpath = Path(file_fullpath.parent, file_fullpath.stem + '_' + file_fullpath.suffix[1:] + '_src')
        if not source_dir_fullpath.exists():
            source_dir_fullpath.mkdir(parents=True)
        else:
            shutil.rmtree(source_dir_fullpath)
        parser.run(file_fullpath, source_dir_fullpath)
        result.append(source_dir_fullpath)
    return result


def add_to_index(dir_fullpaths: list[Path]) -> None:
    git = local['git']
    for dir_fullpath in dir_fullpaths:
        git('add', '--all', str(dir_fullpath))


def remove_from_index(file_fullpaths: list[Path]) -> None:
    git = local['git']

    git('rm', '--cached', *[str(file_fullpath) for file_fullpath in file_fullpaths])


def run(args) -> None:
    logger.enable('cjk_commons')
    logger.enable('parse_1c_build')
    logger.enable(__name__)

    try:
        indexed_file_fullpaths = get_indexed_file_fullpaths()
        if len(indexed_file_fullpaths) == 0:
            logger.info('no added or modified files')
            return

        for_processing_file_fullpaths = get_for_processing_file_fullpaths(indexed_file_fullpaths)
        if len(for_processing_file_fullpaths) == 0:
            logger.info('no for processing files')
            return

        for_indexing_source_dir_fullpaths = parse(for_processing_file_fullpaths)
        if len(for_indexing_source_dir_fullpaths) == 0:
            logger.info('no for indexing source dirs')
            return

        add_to_index(for_indexing_source_dir_fullpaths)

        if not args.keep_files:
            remove_from_index(for_processing_file_fullpaths)
    except Exception as e:
        logger.exception(e)
        sys.exit(1)


def add_subparser(subparsers) -> None:
    decs = 'Pre-commit for 1C:Enterprise files'
    subparser = subparsers.add_parser(
        Path(__file__).stem.replace('_', '-'),
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
        '-k', '--keep-files',
        action='store_true',
        help='Keep 1C-files in the index'
    )

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from configparser import RawConfigParser
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


__version__ = '0.1.0'


def compile_(input_folder: Path, output_file: Path, v8_unpack: Path):  # fixme
    temp_source_folder = Path(tempfile.mkdtemp())
    if not temp_source_folder.exists():
        temp_source_folder.mkdir(parents=True)
    else:
        shutil.rmtree(str(temp_source_folder), ignore_errors=True)

    renames_file = input_folder / 'renames.txt'

    with renames_file.open(encoding='utf-8-sig') as file:
        for line in file:
            names = line.split('-->')

            new_path = temp_source_folder / names[0].strip()
            new_folder_path = new_path.parent

            if not new_folder_path.exists():
                new_folder_path.mkdir(parents=True)

            old_path = input_folder / names[1].strip()

            if old_path.is_dir():
                new_path = temp_source_folder / names[0].strip()
                shutil.copytree(str(old_path), str(new_path))
            else:
                shutil.copy(str(old_path), str(new_path))

    exit_code = subprocess.check_call([
        str(v8_unpack),
        '-B',
        str(temp_source_folder),
        str(output_file)
    ])
    if not exit_code == 0:
        raise Exception('Не удалось собрать файл {}'.format(str(output_file)))


def get_setting(section, key):
    settings_config_file_path_rel = Path('pre-commit-1c.ini')
    if not settings_config_file_path_rel.exists():
        settings_config_file_path_rel = Path(__file__).parent / settings_config_file_path_rel
        if not settings_config_file_path_rel.exists():
            raise Exception('Файл настроек не существует!')
    config = RawConfigParser()
    config.optionxform = lambda option: option
    config.read(str(settings_config_file_path_rel), 'utf-8')
    return config[section][key]


def main():
    argparser = ArgumentParser()
    argparser.add_argument('-v', '--version', action='version', version='%(prog)s, ver. {}'.format(__version__))
    argparser.add_argument('--debug', action='store_true', default=False, help='if this option exists then debug mode '
                                                                               'is enabled')
    argparser.add_argument('input', nargs='?')
    argparser.add_argument('output', nargs='?')
    args = argparser.parse_args()

    if args.debug:
        import sys
        sys.path.append('C:\\Python34\\pycharm-debug-py3k.egg')

        import pydevd
        pydevd.settrace(port=10050)

    v8_unpack = Path(get_setting('General', 'V8Unpack'))
    if not v8_unpack.exists():
        raise Exception('V8Unpack не существует!')

    input_folder = Path(args.input)
    output_file = Path(args.output)
    compile_(input_folder, output_file, v8_unpack)


if __name__ == '__main__':
    sys.exit(main())

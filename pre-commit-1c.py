#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from configparser import RawConfigParser
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


__version__ = '1.0.0'

added_or_modified = re.compile('^\s*(?:A|M)\s+"{0,1}(?P<rel_name>[^"]*)"{0,1}')


def get_added_or_modified_files():
    result = []

    try:
        output = subprocess.check_output(['git', 'status', '--porcelain']).decode('utf-8')
    except subprocess.CalledProcessError:
        return result

    for line in output.split('\n'):
        if line != '':
            match = added_or_modified.match(line)
            if match:
                added_or_modified_file = Path.cwd() / match.group('rel_name')
                if added_or_modified_file.name.lower() != 'readme.md':
                    result.append(added_or_modified_file)

    return result


def get_for_processing_files(files: list):
    result = []

    for file in files:
        if file.suffix.lower() in ['.epf', '.erf', '.ert', '.md']:
            result.append(file)

    return result


def decompile(exe1c: Path, ib: Path, v8_reader: Path, gcomp: Path, files: list):
    result = []

    for file in files:
        source_folder = file.parent / (file.stem + '_' + file.suffix[1:] + '_src')

        if not source_folder.exists():
            source_folder.mkdir(parents=True)
        else:
            shutil.rmtree(str(source_folder), ignore_errors=True)

        with tempfile.NamedTemporaryFile('w', encoding='cp866', suffix='.bat', delete=False) as temp_bat_file:
            temp_bat_file.write('@echo off\n')
            file_suffix_lower = file.suffix.lower()
            if file_suffix_lower in ['.epf', '.erf']:
                temp_bat_file.write('"{}" /F"{}" /DisableStartupMessages /Execute"{}" {}'.format(
                    str(exe1c),
                    str(ib),
                    str(v8_reader),
                    '/C"decompile;pathtocf;{};pathout;{};shutdown;convert-mxl2txt;"'.format(
                        str(file),
                        str(source_folder)
                    )
                ))
            elif file_suffix_lower in ['.ert', '.md']:
                temp_bat_file.write('"{}" -d -F "{}" -DD "{}"'.format(
                    str(gcomp),
                    str(file),
                    str(source_folder)
                ))
        exit_code = subprocess.check_call(['cmd.exe', '/C', str(temp_bat_file.name)])
        if not exit_code == 0:
            raise Exception('Не удалось разобрать файл {}'.format(str(file)))
        result.append(source_folder)
        Path(temp_bat_file.name).unlink()

    return result


def add_to_index(files: list):
    for file in files:
        exit_code = subprocess.check_call(['git', 'add', '--all', str(file)])
        if exit_code != 0:
            exit(exit_code)


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
    args = argparser.parse_args()

    if args.debug:
        import sys
        sys.path.append('C:\\Python34\\pycharm-debug-py3k.egg')

        import pydevd
        pydevd.settrace(port=10050)

    added_or_modified_files = get_added_or_modified_files()
    for_processing_files = get_for_processing_files(added_or_modified_files)
    if len(for_processing_files) == 0:
        exit(0)
    exe1c = Path(get_setting('General', '1C'))
    if not exe1c.exists():
        raise Exception('Платформа не существует!')
    ib = Path(get_setting('General', 'IB'))  # fixme
    if not ib.exists():
        raise Exception('Сервисной информационной базы не существует!')
    v8_reader = Path(get_setting('General', 'V8Reader'))
    if not v8_reader.exists():
        raise Exception('V8Reader не существует!')
    gcomp = Path(get_setting('General', 'GComp'))
    if not gcomp.exists():
        raise Exception('GComp не существует!')
    for_indexing_source_folders = decompile(exe1c, ib, v8_reader, gcomp, for_processing_files)
    add_to_index(for_indexing_source_folders)


if __name__ == '__main__':
    sys.exit(main())
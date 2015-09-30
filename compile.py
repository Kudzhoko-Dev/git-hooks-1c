#!/usr/bin/env python
# -*- coding: utf-8 -*-


def compile_(input_folder: Path, output_file: Path):
    temp_source_folder = Path(tempfile.mkdtemp())
    if not temp_source_folder.exists():
        temp_source_folder.mkdir(parents=True)
    else:
        shutil.rmtree(str(temp_source_folder), ignore_errors=True)

    renames_file = input_folder / 'renames.txt'

    with renames_file.open(encoding='cp866') as file:
        lines = []
        for line in file:
            lines.append(line.split('-->'))
    pass


def main():
    argparser = ArgumentParser()
    argparser.add_argument('-v', '--version', action='version', version='%(prog)s, ver. {}'.format(__version__))
    argparser.add_argument('--debug', action='store_true', default=False, help='if this option exists then debug mode '
                                                                               'is enabled')
    argparser.add_argument('--compile', action='store_true', default=False)
    argparser.add_argument('input_foldername', nargs='?')
    argparser.add_argument('output_filename', nargs='?')
    args = argparser.parse_args()

    if args.debug:
        import sys
        sys.path.append('C:\\Python34\\pycharm-debug-py3k.egg')

        import pydevd
        pydevd.settrace(port=10050)

    if args.compile:
        input_folder = Path(args.input_foldername)
        output_file = Path(args.output_filename)
        compile_(input_folder, output_file)

    else:
        added_or_modified_files = get_added_or_modified_files()
        for_processing_files = get_for_processing_files(added_or_modified_files)
        if len(for_processing_files) == 0:
            exit(0)
        exe_1c = Path(get_setting('General', '1C'))
        if not exe_1c.exists():
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
        for_indexing_source_folders = decompile(exe_1c, ib, v8_reader, gcomp, for_processing_files)
        add_to_index(for_indexing_source_folders)


if __name__ == '__main__':
    sys.exit(main())

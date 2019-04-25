# -*- coding: utf-8 -*-
from pathlib import Path
import os
import pytest
import shutil


from cjk_commons.zip import extract_from_zip
from git_hooks_1c import pre_commit


@pytest.fixture()
def test(request):
    def clean():
        pass

    request.addfinalizer(clean)


def test_pre_commit_1(test):
    dir_fullpath = Path(Path(__file__).parent, 'data')
    file_archived_fullpath = Path(dir_fullpath, '1.zip')
    test_fullpath = Path(dir_fullpath, '1')
    if test_fullpath.exists():
        shutil.rmtree(str(test_fullpath))
    extract_from_zip(file_archived_fullpath, test_fullpath)

    os.chdir(test_fullpath)

    file_fullpaths = pre_commit.get_added_or_modified_file_fullpaths()
    assert len(file_fullpaths) == 0

    assert len(pre_commit.get_for_processing_file_fullpaths(file_fullpaths)) == 0


def test_pre_commit_2(test):
    dir_fullpath = Path(Path(__file__).parent, 'data')
    file_archived_fullpath = Path(dir_fullpath, '2.zip')
    test_fullpath = Path(dir_fullpath, '2')
    if test_fullpath.exists():
        shutil.rmtree(str(test_fullpath))
    extract_from_zip(file_archived_fullpath, test_fullpath)

    os.chdir(test_fullpath)

    file_fullpaths = pre_commit.get_added_or_modified_file_fullpaths()
    assert len(file_fullpaths) == 1

    assert len(pre_commit.get_for_processing_file_fullpaths(file_fullpaths)) == 0


def test_pre_commit_3(test):
    dir_fullpath = Path(Path(__file__).parent, 'data')
    file_archived_fullpath = Path(dir_fullpath, '3.zip')
    test_fullpath = Path(dir_fullpath, '3')
    if test_fullpath.exists():
        shutil.rmtree(str(test_fullpath))
    extract_from_zip(file_archived_fullpath, test_fullpath)

    os.chdir(test_fullpath)

    file_fullpaths = pre_commit.get_added_or_modified_file_fullpaths()
    assert len(file_fullpaths) == 2

    assert len(pre_commit.get_for_processing_file_fullpaths(file_fullpaths)) == 1


def test_pre_commit_4(test):
    dir_fullpath = Path(Path(__file__).parent, 'data')
    file_archived_fullpath = Path(dir_fullpath, '4.zip')
    test_fullpath = Path(dir_fullpath, '4')
    if test_fullpath.exists():
        shutil.rmtree(str(test_fullpath))
    extract_from_zip(file_archived_fullpath, test_fullpath)

    os.chdir(test_fullpath)

    file_fullpaths = pre_commit.get_added_or_modified_file_fullpaths()
    assert len(file_fullpaths) == 2

    for_processing_file_fullpaths = pre_commit.get_for_processing_file_fullpaths(file_fullpaths)

    pre_commit.remove_from_index(for_processing_file_fullpaths)

    file_fullpaths = pre_commit.get_added_or_modified_file_fullpaths()
    assert len(file_fullpaths) == 1

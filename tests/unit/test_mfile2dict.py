import pytest
import os
import tempfile
import json
import yaml
import pickle
from pathlib import Path

from process.io import mfile2dict


@pytest.fixture(scope="module")
def read_mfile():
    """Read-in MFILE for testing.

    :return: parsed mfile
    :rtype: mfile2dict.MFILEParser
    """
    data_path = Path(__file__).parent / "data"
    mfile_path = data_path / "large_tokamak_MFILE.DAT"
    mfile_path_str = str(Path(mfile_path).resolve())

    return mfile2dict.MFILEParser(mfile_path_str)


@pytest.fixture(scope="module")
def temporary_dir():
    return tempfile.mkdtemp()


def test_parser_succeed(read_mfile):
    assert read_mfile._mfile_data


def test_value_read(read_mfile):
    read_mfile.get_parameter_value("xcm013") == 9.7718e-01


def test_write_json(read_mfile, temporary_dir):
    _json_f = os.path.join(temporary_dir, "2017_baseline.json")
    read_mfile.write(_json_f)
    assert os.path.exists(_json_f)
    assert json.load(open(_json_f))


def test_write_yaml(read_mfile, temporary_dir):
    _yml_f = os.path.join(temporary_dir, "2017_baseline.yml")
    read_mfile.write(_yml_f)
    assert os.path.exists(_yml_f)
    assert yaml.load(open(_yml_f), Loader=yaml.BaseLoader)


def test_write_pickle(read_mfile, temporary_dir):
    _pckl_f = os.path.join(temporary_dir, "2017_baseline.pckl")
    read_mfile.write(_pckl_f)
    assert os.path.exists(_pckl_f)
    assert pickle.load(open(_pckl_f, "rb"))

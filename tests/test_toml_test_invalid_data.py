
import os
import glob
import json

import pytest

import toml_tools


from . import decoding_test

# Hardcoded absolute path to run Iron Python tests from \src\
TOML_TEST_DIR = r"C:\Users\James\Documents\Coding\repos\toml-test-master\toml-test-master\tests"


def test_invalid_tests():
    invalid_dir = os.path.join(TOML_TEST_DIR,"invalid")
    for f in os.listdir(invalid_dir):
        if not f.endswith("toml"):
            continue
        with pytest.raises(toml_tools.TomlDecodeError):
            with open(os.path.join(invalid_dir, f)) as fh:
                toml_tools.load(fh)

def make_errors_correctly_test(toml_path):
    def test_errors_on_invalid_toml():
        with pytest.raises(toml_tools.TomlDecodeError):
            with open(toml_path,'rt') as toml_fh:
                toml_tools.load(toml_fh)
    return test_errors_on_invalid_toml


TOML_INVALID_GLOB = os.path.join(TOML_TEST_DIR,"invalid", '**\*.toml')
for file_path in glob.iglob(TOML_INVALID_GLOB):
    test_name = os.path.splitext(os.path.basename(file_path))[0]
    test_func_name = 'test_toml_test_invalid_%s' % test_name

    # It would be cleaner to setattr these test functions as class methods, 
    # but ironpython-pytest doesn't look for class methods as yet.
    globals()[test_func_name] = make_errors_correctly_test(file_path)
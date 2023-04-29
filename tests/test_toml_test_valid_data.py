
import os
import glob
import json

import pytest


FLAGS = 'rt'

import toml_tools
# import tomlkit as toml_tools
# import toml as toml_tools

# FLAGS = 'rb'
# import tomllib as toml_tools
# import tomli as toml_tools


from . import decoding_test

# Hardcoded absolute path to run Iron Python tests from \src\
TOML_TEST_DIR = r"C:\Users\James\Documents\Coding\repos\toml-test-master\toml-test-1.0.0\tests"

VALID_DIR = os.path.join(TOML_TEST_DIR,"valid")

# def test_valid_tests():
#     for f in os.listdir(VALID_DIR):
#         if not f.endswith("toml"):
#             continue
#         with open(os.path.join(VALID_DIR, f)) as fh:
#             toml_tools.dumps(toml_tools.load(fh))



def make_parses_correctly_test(toml_path):
    def test_parses_toml_to_tagged_json_from():
        json_path = os.path.splitext(toml_path)[0] + '.json'
        if not os.path.exists(json_path):
            raise FileExistsError('No json test file for toml file: %s' % toml_path)
        
        


        with open(toml_path, FLAGS) as toml_fh, open(json_path,'rt', encoding = 'utf8') as json_fh:
            dict_ = toml_tools.load(toml_fh)
            # print(f'{dict_=}')
            # tagged = decoding_test.tag(dict_)
            # jsoned = json.dumps(tagged)
            expected = json.load(json_fh) #json_fh.read()
            # print(f'{expected=}')
            # assert tagged == expected

            de_tagged = decoding_test.de_tag(expected)
            assert de_tagged == dict_
    return test_parses_toml_to_tagged_json_from


TOML_VALID_GLOB = os.path.join(TOML_TEST_DIR,"valid", r'**\*.toml')
for file_path in glob.iglob(TOML_VALID_GLOB):
    test_name = os.path.splitext(os.path.basename(file_path))[0].replace('-','_')

    # if test_name != 'case_sensitive':
    #     continue

    test_func_name = 'test_toml_test_valid_%s' % test_name

    # It would be cleaner to setattr these test functions as class methods, 
    # but ironpython-pytest doesn't look for class methods as yet.
    globals()[test_func_name] = make_parses_correctly_test(file_path)

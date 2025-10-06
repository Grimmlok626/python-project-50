from hexlet_code.gendiff import generate_diff
import sys
import os
import json


def test_compare_json_files():
    base_dir = os.path.dirname(__file__)
    file1_path = os.path.join(base_dir, "test_data", "file1.json")
    file2_path = os.path.join(base_dir, "test_data", "file2.json")
    expected_path = os.path.join(base_dir, "test_data", "expected_output.txt")

    with open(expected_path, "r") as f:
        expected = f.read().strip()

    # Вызов с путями, а не со словарями
    result = generate_diff(file1_path, file2_path)

    print("Generated diff:\n", result)
    assert result == expected


def test_compare_yaml_files():
    filepath1 = 'tests/test_data/file1.yml'
    filepath2 = 'tests/test_data/file2.yml'
    expected_output = """{
  - follow: false
  host: hexlet.io
  proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    result = generate_diff(filepath1, filepath2)
    print("Result:\n", result)
    assert result == expected_output
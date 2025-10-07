import os
from hexlet_code.gendiff import generate_diff

BASE_DIR = os.path.dirname(__file__)
TEST_DATA_DIR = os.path.join(BASE_DIR, "test_data")


def test_compare_json_files():
    BASE_DIR = os.path.dirname(__file__)
    TEST_DATA_DIR = os.path.join(BASE_DIR, "test_data")
    file1_path = os.path.join(TEST_DATA_DIR, "file1.json")
    file2_path = os.path.join(TEST_DATA_DIR, "file2.json")
    expected_path = os.path.join(TEST_DATA_DIR, "expected_output_json.txt")
    with open(expected_path, "r", encoding="utf-8") as f:
        expected = f.read().strip()
    result = generate_diff(file1_path, file2_path)

    print("Expected output:")
    print(expected)
    print("\nGenerated diff:")
    print(result)
    print("\n=== DEBUG: Result ===")
    print(result)

    assert result == expected


def test_compare_yaml_files():
    BASE_DIR = os.path.dirname(__file__)
    TEST_DATA_DIR = os.path.join(BASE_DIR, "test_data")
    file1_path = os.path.join(TEST_DATA_DIR, "file1.yml")
    file2_path = os.path.join(TEST_DATA_DIR, "file2.yml")
    expected_path = os.path.join(TEST_DATA_DIR, "expected_output_yaml.txt")
    with open(expected_path, "r", encoding="utf-8") as f:
        expected = f.read().strip()
    result = generate_diff(file1_path, file2_path)

    print("Expected output:")
    print(expected)
    print("\nGenerated diff:")
    print(result)
    
    assert result == expected
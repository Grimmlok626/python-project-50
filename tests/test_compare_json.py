from hexlet_code.gendiff import generate_diff
import sys
import os
import json

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)


def test_compare_json_files():
    base_dir = os.path.dirname(__file__)
    file1_path = os.path.join(base_dir, "test_data", "file1.json")
    file2_path = os.path.join(base_dir, "test_data", "file2.json")
    expected_path = os.path.join(base_dir, "test_data", "expected_output.txt")

    with open(expected_path, "r") as f:
        expected = f.read().strip()

    # Загружаем файлы в словари с использованием контекстных менеджеров
    with open(file1_path, "r") as f:
        data1 = json.load(f)
    with open(file2_path, "r") as f:
        data2 = json.load(f)

    # Вызов вашей функции
    result = generate_diff(data1, data2)
    print("Generated diff:\n", result)

    assert result.strip() == expected

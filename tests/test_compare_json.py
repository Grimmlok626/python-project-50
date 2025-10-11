import os
import json
from hexlet_code import generate_diff

BASE_DIR = os.path.dirname(__file__)
TEST_DATA_DIR = os.path.join(BASE_DIR, "test_data")


def test_compare_json_files():
    file1_path = os.path.join(TEST_DATA_DIR, "file1.json")
    file2_path = os.path.join(TEST_DATA_DIR, "file2.json")
    expected_path = os.path.join(TEST_DATA_DIR, "expected_output_json.txt")
    
    # Читаем файл с ожидаемым JSON-выводом, он должен быть корректным JSON
    with open(expected_path, "r", encoding="utf-8") as f:
        expected_str = f.read()

    # Генерируем результат с указанием формата 'json'
    result_str = generate_diff(file1_path, file2_path, format='json')

    # Загружаем оба результата как JSON структуры
    result_json = json.loads(result_str)
    expected_json = json.loads(expected_str)

    # Сравниваем структурированные данные
    assert result_json == expected_json


def test_compare_yaml_files():
    file1_path = os.path.join(TEST_DATA_DIR, "file1.yml")
    file2_path = os.path.join(TEST_DATA_DIR, "file2.yml")
    expected_path = os.path.join(TEST_DATA_DIR, "expected_output_yaml.txt")
    
    # Читаем ожидаемый вывод (предполагается, что он тоже в формате текста, можно оставить как есть)
    with open(expected_path, "r", encoding="utf-8") as f:
        expected = f.read().strip()
    result = generate_diff(file1_path, file2_path)

    print("Expected output:")
    print(expected)
    print("\nGenerated diff:")
    print(result)
    
    assert result == expected
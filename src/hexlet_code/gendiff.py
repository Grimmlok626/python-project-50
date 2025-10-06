import argparse
import json
import os
from .parsers import parse_yaml


def parse_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.yaml', '.yml']:
        return parse_yaml(file_path)
    elif ext == '.json':
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        raise ValueError("Unsupported file extension")


def generate_diff(filepath1, filepath2):
    """
    Генерирует строковое представление различий между двумя файлами.

    Args:
        filepath1 (str): путь к первому файлу
        filepath2 (str): путь ко второму файлу

    Returns:
        str: строка с результатом сравнения
    """
    data1 = parse_file(filepath1)
    data2 = parse_file(filepath2)

    all_keys = sorted(data1.keys() | data2.keys())
    lines = ['{']
    for key in all_keys:
        if key not in data1:
            lines.append(f"  + {key}: {format_value(data2[key])}")
        elif key not in data2:
            lines.append(f"  - {key}: {format_value(data1[key])}")
        else:
            if data1[key] == data2[key]:
                lines.append(f"  {key}: {format_value(data1[key])}")
            else:
                lines.append(f"  - {key}: {format_value(data1[key])}")
                lines.append(f"  + {key}: {format_value(data2[key])}")
    lines.append('}')
    return '\n'.join(lines)


def format_value(value):
    """
    Форматирует значение для вывода.

    Args:
        value: значение любого типа

    Returns:
        str: форматированное представление
    """
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, (list, dict)):
        return json.dumps(value)
    else:
        return str(value)


def main():
    parser = argparse.ArgumentParser(
        description="Сравнивает два файла конфигурации и выводит разницу."
    )
    parser.add_argument("first_file", type=str, help="Путь к первому файлу")
    parser.add_argument("second_file", type=str, help="Путь ко второму файлу")
    parser.add_argument(
        "-f",
        "--format",
        dest="format",
        type=str,
        default="plain",
        help='формат вывода, пока поддерживается только "plain"',
    )

    args = parser.parse_args()

    diff_result = generate_diff(args.first_file, args.second_file)
    print(diff_result)


if __name__ == "__main__":
    main()
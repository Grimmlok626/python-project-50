import argparse
import json

def parse_file(file_path):
    """
    Загружает JSON из файла по указанному пути.

    Args:
        file_path (str): путь к файлу

    Returns:
        dict: данные из файла

    Raises:
        FileNotFoundError: если файл не найден
        json.JSONDecodeError: если содержимое файла некорректный JSON
    """
    try:
        with open(file_path, encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        raise
    except json.JSONDecodeError:
        print(f"Некорректный JSON в файле: {file_path}")
        raise

def generate_diff(data1, data2):
    """
    Генерирует строковое представление различий между двумя словарями.

    Args:
        data1 (dict): первый словарь
        data2 (dict): второй словарь

    Returns:
        str: строка с результатом сравнения
    """
    all_keys = sorted(data1.keys() | data2.keys())
    lines = ['{']
    for key in all_keys:
        if key not in data1:
            lines.append(f"  + {key}: {format_value(data2[key])}")  # 2 пробела
        elif key not in data2:
            lines.append(f"  - {key}: {format_value(data1[key])}")  # 2 пробела
        else:
            if data1[key] == data2[key]:
                lines.append(f"  {key}: {format_value(data1[key])}")  # 2 пробела
            else:
                lines.append(f"  - {key}: {format_value(data1[key])}")  # 2 пробела
                lines.append(f"  + {key}: {format_value(data2[key])}")  # 2 пробела
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
    elif isinstance(value, list):
        return json.dumps(value)
    elif isinstance(value, dict):
        return json.dumps(value)
    else:
        return str(value)


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=str, help="Path to the first file")
    parser.add_argument("second_file", type=str, help="Path to the second file")
    parser.add_argument(
        "-f",
        "--format",
        dest="format",
        type=str,
        default="plain",
        help='set format of output, only "plain" supported for now',
    )

    args = parser.parse_args()

    data1 = parse_file(args.first_file)
    data2 = parse_file(args.second_file)

    diff_result = generate_diff(data1, data2)
    print(diff_result)


if __name__ == "__main__":
    main()

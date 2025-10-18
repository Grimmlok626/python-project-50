import os
import json
import argparse
from .parsers import parse_yaml
from gendiff.formatters import FORMATTERS


def parse_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext in ['.yaml', '.yml']:
        return parse_yaml(filepath)
    elif ext == '.json':
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")


def build_diff_tree(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    nodes = []

    for key in keys:
        if key not in data1:
            nodes.append({'key': key, 'status': 'added', 'value': data2[key]})
        elif key not in data2:
            nodes.append({'key': key, 'status': 'removed', 'value': data1[key]})
        else:
            v1 = data1[key]
            v2 = data2[key]
            if isinstance(v1, dict) and isinstance(v2, dict):
                children = build_diff_tree(v1, v2)
                nodes.append(
                    {'key': key, 'status': 'nested', 'children': children}
                )
            elif v1 == v2:
                nodes.append({'key': key, 'status': 'unchanged', 'value': v1})
            else:
                nodes.append(
                    {'key': key, 'status': 'updated', 'value': (v1, v2)}
                )
    return nodes


def validate_diff_tree(nodes):
    assert isinstance(nodes, list), 'diff_tree должно быть списком'
    for node in nodes:
        assert isinstance(node, dict), (
            'Каждый элемент diff_tree должен быть словарем'
        )
        assert 'key' in node and 'status' in node, (
            "Узел должен содержать 'key' и 'status'"
        )

        status = node['status']
        if status == 'nested':
            assert 'children' in node, "Узел с 'nested' должен иметь 'children'"
            validate_diff_tree(node['children'])
        elif status in ('added', 'removed', 'unchanged'):
            assert 'value' in node, (
                f"Узел со статусом '{status}' должен иметь 'value'"
            )
        elif status == 'updated':
            assert (
                'value' in node and
                isinstance(node['value'], (list, tuple)) and
                len(node['value']) == 2
            ), 'Узел "updated" должен иметь список или кортеж из двух элементов'
        else:
            raise ValueError(f"Неизвестный статус узла: {status}")


def generate_diff(filepath1, filepath2, format='stylish'):
    data1 = parse_file(filepath1)
    data2 = parse_file(filepath2)
    diff_tree = build_diff_tree(data1, data2)

    validate_diff_tree(diff_tree)

    formatter = FORMATTERS.get(format)
    if not formatter:
        raise ValueError(f"Unknown format: {format}")
    return formatter(diff_tree)


def main():
    parser = argparse.ArgumentParser(description='Compare two files.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='Output format (stylish, plain, json)'
    )
    args = parser.parse_args()

    output = generate_diff(args.first_file, args.second_file, args.format)
    print(output)


if __name__ == '__main__':
    main()
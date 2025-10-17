import json


def stylish(tree):
    def format_value(value, depth):
        # Примитивы
        if not isinstance(value, dict):
            if value is None:
                return 'null'
            if isinstance(value, bool):
                return str(value).lower()
            if isinstance(value, (int, float)):
                return str(value)
            return value
        # Словарь → многострочный блок
        lines = ['{']
        indent_children = '    ' * (depth)
        indent_closing = '    ' * (depth - 1)
        for k, v in sorted(value.items()):
            lines.append(f"{indent_children}{k}: {format_value(v, depth + 1)}")
        lines.append(f"{indent_closing}}}")
        return '\n'.join(lines)

    def iter(nodes, depth=1):
        lines = []
        indent = '    ' * depth
        sign_indent = '    ' * (depth - 1) + '  '
        for node in nodes:
            key = node['key']
            status = node['status']
            if status == 'nested':
                # вложенный узел
                subtree = iter(node['children'], depth + 1)
                lines.append(f"{indent}{key}: {subtree}")
            elif status == 'added':
                lines.append(f"{sign_indent}+ {key}: {format_value(node['value'], depth + 1)}")
            elif status == 'removed':
                lines.append(f"{sign_indent}- {key}: {format_value(node['value'], depth + 1)}")
            elif status == 'unchanged':
                lines.append(f"{indent}{key}: {format_value(node['value'], depth + 1)}")
            elif status == 'updated':
                old, new = node['value']
                lines.append(f"{sign_indent}- {key}: {format_value(old, depth + 1)}")
                lines.append(f"{sign_indent}+ {key}: {format_value(new, depth + 1)}")
        closing = '    ' * (depth - 1)
        return '{\n' + '\n'.join(lines) + f'\n{closing}}}'

    return iter(tree)


def plain(tree):
    def build_path(node, ancestors):
        return '.'.join(ancestors + [node['key']])
    
    def format_node(node, ancestors):
        path = build_path(node, ancestors)
        status = node['status']
        lines = []

        if status == 'nested':
            for child in node['children']:
                lines.extend(format_node(child, ancestors + [node['key']]))
            return lines

        elif status == 'added':
            value_str = stringify_value(node['value'])
            lines.append(f"Property '{path}' was added with value: {value_str}")
        elif status == 'removed':
            lines.append(f"Property '{path}' was removed")
        elif status == 'updated':
            old_value, new_value = node['value']
            old_str = stringify_value(old_value)
            new_str = stringify_value(new_value)
            lines.append(f"Property '{path}' was updated. From {old_str} to {new_str}")
        elif status == 'unchanged':
            # ничего не делаем, по задаче не требует
            pass
        return lines

    def stringify_value(value):
        if isinstance(value, dict) or isinstance(value, list):
            return '[complex value]'
        if value is None:
            return 'null'
        if isinstance(value, bool):
            return str(value).lower()
        if isinstance(value, (int, float)):
            return str(value)
        if isinstance(value, str):
            return f"'{value}'"   # Добавляем кавычки вокруг строк
        return str(value)

    lines = []
    for node in tree:
        lines.extend(format_node(node, []))
    return '\n'.join(lines)


def json_format(tree):
    return json.dumps(tree, ensure_ascii=False, indent=2)

        
FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_format,  # Добавили JSON формат
}
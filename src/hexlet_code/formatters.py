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
            return value  # строка или другой тип — str(value) можно добавить, но в тестах только строки и числа

        # Словарь → многострочный блок
        lines = ['{']
        indent_children = '    ' * depth
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

FORMATTERS = {
    'stylish': stylish,
}
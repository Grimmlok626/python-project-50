import json


def stylish(tree):
    def format_value(value, depth):
        if not isinstance(value, dict):
            if value is None:
                return 'null'
            if isinstance(value, bool):
                return str(value).lower()
            if isinstance(value, (int, float)):
                return str(value)
            return value

        lines = ['{']
        indent_children = '    ' * depth
        indent_closing = '    ' * (depth - 1)
        for k, v in sorted(value.items()):
            lines.append(f"{indent_children}{k}: {format_value(v, depth + 1)}")
        lines.append(f"{indent_closing}}}")
        return '\n'.join(lines)

    def process_added(node, depth, sign_indent):
        return f"{sign_indent}+ {node['key']}: {format_value(node['value'], depth + 1)}"

    def process_removed(node, depth, sign_indent):
        return f"{sign_indent}- {node['key']}: {format_value(node['value'], depth + 1)}"

    def process_unchanged(node, depth, indent):
        return f"{indent}{node['key']}: {format_value(node['value'], depth + 1)}"

    def process_updated(node, depth, sign_indent):
        old, new = node['value']
        line_removed = f"{sign_indent}- {node['key']}: {format_value(old, depth + 1)}"
        line_added = f"{sign_indent}+ {node['key']}: {format_value(new, depth + 1)}"
        return [line_removed, line_added]

    def iter(nodes, depth=1):
        lines = []
        indent = '    ' * depth
        sign_indent = '    ' * (depth - 1) + '  '
        for node in nodes:
            status = node['status']

            if status == 'nested':
                subtree = iter(node['children'], depth + 1)
                lines.append(f"{indent}{node['key']}: {subtree}")
            elif status == 'added':
                lines.append(process_added(node, depth, sign_indent))
            elif status == 'removed':
                lines.append(process_removed(node, depth, sign_indent))
            elif status == 'unchanged':
                lines.append(process_unchanged(node, depth, indent))
            elif status == 'updated':
                lines.extend(process_updated(node, depth, sign_indent))
        closing = '    ' * (depth - 1)
        return '{\n' + '\n'.join(lines) + f'\n{closing}}}'

    return iter(tree)


def plain(tree):
    def build_path(node, ancestors):
        return '.'.join(ancestors + [node['key']])

    def stringify_value(value):
        if isinstance(value, (dict, list)):
            return '[complex value]'
        if value is None:
            return 'null'
        if isinstance(value, bool):
            return str(value).lower()
        if isinstance(value, (int, float)):
            return str(value)
        if isinstance(value, str):
            return f"'{value}'"
        return str(value)

    def format_added(node, path):
        value_str = stringify_value(node['value'])
        return f"Property '{path}' was added with value: {value_str}"

    def format_removed(path):
        return f"Property '{path}' was removed"

    def format_updated(node, path):
        old_value, new_value = node['value']
        old_str = stringify_value(old_value)
        new_str = stringify_value(new_value)
        return f"Property '{path}' was updated. From {old_str} to {new_str}"

    def format_node(node, ancestors):
        status = node['status']
        path = build_path(node, ancestors)

        if status == 'nested':
            lines = []
            for child in node['children']:
                lines.extend(format_node(child, ancestors + [node['key']]))
            return lines
        if status == 'added':
            return [format_added(node, path)]
        if status == 'removed':
            return [format_removed(path)]
        if status == 'updated':
            return [format_updated(node, path)]
        if status == 'unchanged':
            return []
        return []

    lines = []
    for node in tree:
        lines.extend(format_node(node, []))
    return '\n'.join(lines)


def json_format(tree):
    return json.dumps(tree, ensure_ascii=False, indent=2)


FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_format,
}
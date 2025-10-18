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


def plain(tree):
    lines = []
    for node in tree:
        lines.extend(format_node(node, []))
    return '\n'.join(lines)

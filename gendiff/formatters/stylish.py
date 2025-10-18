def format_value(value, depth):
    if not isinstance(value, dict):
        if value is None:
            return 'null'
        if isinstance(value, bool):
            return str(value).lower()
        if isinstance(value, (int, float)):
            return str(value)
        return str(value)  # возвращаем строку

    lines = ['{']
    indent_children = '    ' * depth
    indent_closing = '    ' * (depth - 1)
    for k, v in sorted(value.items()):
        formatted = format_value(v, depth + 1)
        lines.append(
            f"{indent_children}{k}: {formatted}"
        )
    lines.append(f"{indent_closing}}}")
    return '\n'.join(lines)


def process_added(node, depth, sign_indent):
    return (
        f"{sign_indent}+ {node['key']}: "
        f"{format_value(node['value'], depth + 1)}"
    )


def process_removed(node, depth, sign_indent):
    return (
        f"{sign_indent}- {node['key']}: "
        f"{format_value(node['value'], depth + 1)}"
    )


def process_unchanged(node, depth, indent):
    return (
        f"{indent}{node['key']}: "
        f"{format_value(node['value'], depth + 1)}"
    )


def process_updated(node, depth, sign_indent):
    old, new = node['value']
    line_removed = (
        f"{sign_indent}- {node['key']}: "
        f"{format_value(old, depth + 1)}"
    )
    line_added = (
        f"{sign_indent}+ {node['key']}: "
        f"{format_value(new, depth + 1)}"
    )
    return [line_removed, line_added]


def stylish(tree):
    def iter_(nodes, depth=1):
        lines = []
        indent = '    ' * depth
        sign_indent = '    ' * (depth - 1) + '  '
        for node in nodes:
            status = node['status']

            if status == 'nested':
                subtree = iter_(node['children'], depth + 1)
                lines.append(
                    f"{indent}{node['key']}: {subtree}"
                )
            elif status == 'added':
                lines.append(process_added(node, depth, sign_indent))
            elif status == 'removed':
                lines.append(process_removed(node, depth, sign_indent))
            elif status == 'unchanged':
                lines.append(process_unchanged(node, depth, indent))
            elif status == 'updated':
                lines.extend(process_updated(node, depth, sign_indent))
        closing = '    ' * (depth - 1)
        result = (
            '{\n' +
            '\n'.join(lines) +
            f'\n{closing}}}'
        )
        return result

    return iter_(tree)
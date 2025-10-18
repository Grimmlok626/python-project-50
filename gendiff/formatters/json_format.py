import json


def json_format(tree):
    return json.dumps(tree, ensure_ascii=False, indent=2)

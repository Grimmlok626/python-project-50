from .stylish import stylish
from .plain import plain
from .json_format import json_format


FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_format,
}
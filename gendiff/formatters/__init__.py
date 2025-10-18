from .json_format import json_format
from .plain import plain
from .stylish import stylish

FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': json_format,
}
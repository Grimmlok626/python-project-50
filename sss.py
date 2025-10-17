from gendiff.scripts.gendiff import generate_diff

with open('actual_plain_output.txt', 'w', encoding='utf-8') as f:
    result = generate_diff(
        'tests/test_data/file1.json',
        'tests/test_data/file2.json',
        format='plain'
    )
    f.write(result)

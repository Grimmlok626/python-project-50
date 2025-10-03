import argparse
import json

def parse_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)

def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str, help='Path to the first file')
    parser.add_argument('second_file', type=str, help='Path to the second file')
    parser.add_argument(
        '-f',
        '--format',
        dest='format',
        type=str,
        default='plain',
        help='set format of output'
    )

    args = parser.parse_args()

    # Читаем и парсим файлы перед сравнением
    data1 = parse_file(args.first_file)
    data2 = parse_file(args.second_file)

    # Для проверки выводим считанные данные
    print('Data from first file:', data1)
    print('Data from second file:', data2)

    # Тут далее вы бы вызвали функцию сравнения и вывод результата

if __name__ == '__main__':
    main()
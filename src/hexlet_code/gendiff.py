import argparse

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

    # Здесь вы можете добавить вызов функции сравнения файлов,
    # передав ей args.first_file, args.second_file, args.format

    print(f'File 1: {args.first_file}')
    print(f'File 2: {args.second_file}')
    print(f'Selected format: {args.format}')

if __name__ == '__main__':
    main()
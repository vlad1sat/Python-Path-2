import os
from collections.abc import Iterable


def get_count_strings(directory: str) -> Iterable[tuple]:
    for path, directories, files_dir in os.walk(directory):
        for file in files_dir:
            count = 0
            if file.endswith('.py'):
                path_file = os.path.join(path, file)
                with open(path_file, 'r', encoding='utf-8') as curr_file:
                    for line in curr_file:
                        if line == '\n' or line.startswith('"') or line.startswith('#'):
                            continue
                        count += 1
                    yield path_file, count


for file_dir in get_count_strings('..'):
    print("Файл \"{0}\". Количество строк кода: {1}".format(file_dir[0], file_dir[1]))
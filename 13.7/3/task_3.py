import os
from typing import Iterable


def find_dir(directory: str, find_file: str) -> Iterable[str]:
    for path, directories, files in os.walk(directory):
        for file in files:
            yield os.path.join(path, file)
            if file == find_file:
                return


for file_dir in find_dir('..', 'task_3.py'):
    print(file_dir)


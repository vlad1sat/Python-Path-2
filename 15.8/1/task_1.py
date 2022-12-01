from msilib.schema import File as UserFile


class File:

    def __init__(self, filename: str, mode: str) -> None:
        self.__file_name = filename
        self.__mode = mode
        self.__file = None

    def __enter__(self) -> UserFile:
        self.__file = open(self.__file_name, self.__mode)
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.__file.close()


with File('my_file.txt', 'w') as file:
    file.write('task_1')

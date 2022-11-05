import os


def create_file():
    file = open(path, 'w', encoding='utf-8')
    file.write(information)
    file.close()
    print(f"\nСодержимое файла:\n{information}")


information = input("Введите строку: ")
user_path = input("Куда хотите сохранить документ? Введите последовательность папок (через пробел): ").split()
name_file = input("\nВведите имя файла: ")
path = os.path.join(*user_path, name_file)
if os.path.exists(path):
    command = input("Вы действительно хотите перезаписать файл? ").lower()
    if command == 'нет':
        exit()
    if command == 'да':
        print("Файл успешно перезаписан!")
        create_file()
else:
    print("Файл успешно сохранён!")
    create_file()

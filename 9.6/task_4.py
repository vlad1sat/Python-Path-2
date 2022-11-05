import os


def study_dir(path):
    for elem_address in os.listdir(path):
        if os.path.isdir(elem_address):
            information['count_dir'] += 1
            study_dir(elem_address)
        else:
            information['count_files'] += 1


address = input("Введите путь до каталога: ")
information = {
    'count_files': 0,
    'count_dir': 0
}

study_dir(address)
print("Размер каталога (в Кб):", round(os.path.getsize(address) / 1024))
print("Количество подкаталогов:", information['count_dir'])
print("Количество файлов:", information['count_files'])


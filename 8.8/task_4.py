import sys


def find_key(struct: dict, key_struct: str, depth: int = sys.maxsize):
    if key_struct in struct:
        return struct[key_struct]
    if depth > 1:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key_struct, depth - 1)
                if result:
                    break
        else:
            result = None
        return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input('Введите искомый ключ: ')
command = input("Хотите ввести максимальную глубину? Y/N: ").upper()
if command == 'N':
    print('Значение ключа:', find_key(site, key))
elif command == 'Y':
    depth_site = int(input("Введите максимальную глубину: "))
    print('Значение ключа:', find_key(site, key, depth_site))



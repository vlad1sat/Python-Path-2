count_symbols = 0
with open('people.txt', 'r', encoding='utf-8') as names:
    for name in names:
        name = name.replace('\n', '')
        try:
            count_symbols += len(name)
            if len(name) < 5:
                raise BaseException
        except BaseException:
            print("Ошибка: менее трёх символов в строке 5.")

print("Общее количество символов:", count_symbols)
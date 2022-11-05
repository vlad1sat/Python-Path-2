import random

all_number = 0
with open('out_file.txt', 'w', encoding='utf-8') as numbers:
    try:
        while all_number < 777:
            random_number = random.randint(1, 13)
            if random_number == 1:
                raise BaseException
            number = input("Введите число: ")
            numbers.write(''.join([number, '\n']))
            all_number += int(number)
        print("Вы успешно выполнили условие для выхода из порочного цикла!\n")
    except BaseException:
        print("Вас постигла неудача!\n")

with open('out_file.txt', 'r', encoding='utf-8') as numbers_txt:
    for number_txt in numbers_txt:
        print(number_txt, end='')

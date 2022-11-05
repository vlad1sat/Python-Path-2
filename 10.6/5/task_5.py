import pandas
import numexpr as ne


result = 0
with open('calc.txt', 'r', encoding='utf-8') as calc:
    for line in calc:
        line = line.replace('\n', '')
        try:
            pandas.eval(line)
        except Exception:
            command = input(f"Обнаружена ошибка в строке: {line}  Хотите исправить? ").lower()
            if command == 'да':
                new_line = input("Введите исправленную строку: ")
                result += ne.evaluate(new_line)
        else:
            result += ne.evaluate(line)

print("Сумма результатов:", result)
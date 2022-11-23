end_range = int(input("Введите до какого числа производить вычисление: "))
collection = (num ** 2 for num in range(end_range))
for num in collection:
    print(num)

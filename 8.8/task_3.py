def number_fibonacci(position):
    if position == 1 or position == 2:
        return 1
    return number_fibonacci(position - 1) + number_fibonacci(position - 2)


position_number = int(input("Введите позицию числа в ряде Фибоначчи: "))
print("Число:", number_fibonacci(position_number))

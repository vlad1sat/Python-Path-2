def generate_collection(end_nums):
    for number in range(end_nums):
        yield number ** 2


end_range = int(input("Введите до какого числа производить вычисление: "))
collection = generate_collection(end_nums=end_range)
for num in collection:
    print(num)
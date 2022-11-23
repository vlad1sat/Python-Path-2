def get_sum():
    for first_number in list_1:
        for second_number in list_2:
            yield first_number, second_number, first_number * second_number


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

for result in get_sum():
    print(str(result).replace('(', '').replace(')', ''))
    if result[2] == to_find:
        print('Found!!!')
        break

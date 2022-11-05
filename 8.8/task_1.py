def get_num(num):
    if num >= 1:
        get_num(num - 1)
        print(num)


number = int(input("Введите num: "))
get_num(number)
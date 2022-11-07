def hanoi_towers(discs, first_kernel, second_kernel):
    if discs == 1:
        print("Переложить диск 1 со стержня номер {} на стержень номер {}".format(first_kernel,
                                                                                  second_kernel))
    else:
        tower = 6 - first_kernel - second_kernel
        hanoi_towers(discs - 1, first_kernel, tower)
        print("Переложить диск {} со стержня номер {} на стержень номер {}".format(discs,
                                                                                   first_kernel,
                                                                                   second_kernel))
        hanoi_towers(discs - 1, tower, second_kernel)


count_discs = int(input("Введите количество дисков: "))
hanoi_towers(count_discs, 1, 2)
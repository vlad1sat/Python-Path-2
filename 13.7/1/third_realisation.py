class PowNumbers:

    def __init__(self, limit):
        self.__limit = limit
        self.element = -1

    def __iter__(self):
        self.element = -1
        return self

    def __next__(self):
        self.element += 1
        if self.element < self.__limit:
            return self.element ** 2
        raise StopIteration


end_range = int(input("Введите до какого числа производить вычисление: "))
collection = PowNumbers(limit=end_range)
for num in collection:
    print(num)

from collections.abc import Iterable


def get_q_hofstadter(numbers: list) -> Iterable[int]:
    if numbers[0] != 1 or numbers[1] != 1 or len(numbers) != 2:
        print("Некорректная последовательность!")
        exit()
    q_hofstadter = numbers[:]
    n = 2
    while True:
        number = q_hofstadter[n - q_hofstadter[n - 1]] + q_hofstadter[n - q_hofstadter[n - 2]]
        q_hofstadter.append(number)
        n += 1
        yield number


for num in get_q_hofstadter([1, 1]):
    print(num)

from collections import Counter


def can_be_poly(word: str) -> bool:
    return len(word) % 2 == sum(symbol % 2 for symbol in Counter(word).values())


if __name__ == '__main__':
    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))

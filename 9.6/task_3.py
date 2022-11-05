import os
import string


def count_symbols(line):
    symbols_line = 0
    for _ in line:
        symbols_line += 1
    return symbols_line


def count_words(line):
    return len(line.split())


def create_dict():
    list_symbols = list(string.ascii_lowercase)
    new_dict = dict()
    for symbol in list_symbols:
        new_dict[symbol] = 0
    return new_dict


def count_letters(line):
    for symbol in line:
        if symbol in letters:
            letters[symbol] += 1


def get_min_letter():
    min_letter = ''
    max_count = max(letters.values())
    for letter, count_letter in letters.items():
        if count_letter <= 0:
            continue
        if count_letter < max_count:
            min_letter = letter
            max_count = count_letter
    return min_letter


zen_file = open(os.path.abspath(os.path.join('', '2', 'zen.txt')))
symbols = 0
words = 0
lines = 0
letters = create_dict()
for zen_line in zen_file:
    zen_line = zen_line.replace('\n', '').lower()
    symbols += count_symbols(zen_line)
    words += count_words(zen_line)
    count_letters(zen_line)
    if zen_line != '':
        lines += 1

print("Количество букв в файле:", symbols)
print("Количество слов в файле:", words)
print("Количество строк в файле:", lines)
print("Наиболее редкая буква:", get_min_letter())



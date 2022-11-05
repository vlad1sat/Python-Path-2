import string


def create_dict():
    list_symbols = list(string.ascii_lowercase)
    new_dict = dict()
    for letter in list_symbols:
        new_dict[letter] = 0
    return new_dict


def logic_letters():
    count = 0
    for symbol in text:
        if symbol.isalpha():
            count += 1
            letters[symbol] += 1
    return count


text_file = open('text.txt', 'r', encoding='utf-8')
text = text_file.read().lower()
letters = create_dict()
count_letters = logic_letters()
text_file.close()

correct_dict = {(letter, value) for letter, value in letters.items() if value != 0}
sort_dict = sorted(correct_dict, key=lambda value: (-value[1], value[0]))

analyst = open('analysis.txt', 'w', encoding='utf-8')
print("Содержимое файла analysis.txt:")
for sort_value in sort_dict:
    information = "{} {}\n".format(sort_value[0], round(sort_value[1] / count_letters, 3))
    analyst.write(information)
    print(information, end='')


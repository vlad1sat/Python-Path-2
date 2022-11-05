import string


def encrypt_file():
    content = ''
    index_line = 0
    for element_text in elements_text:
        index_line += 1
        for symbol in element_text:
            if symbol.isalpha():
                encrypt_symbol_index = string.ascii_letters.index(symbol) + index_line
                content = ''.join([content, string.ascii_letters[encrypt_symbol_index]])
            else:
                content = ''.join([content, symbol])
        content = ''.join([content, '\n'])
    file_encrypt = open('cipher_text.txt', 'w', encoding='utf-8')
    file_encrypt.write(content)
    file_encrypt.close()


text_file = open('text.txt', 'r', encoding='utf-8')
elements_text = []
for line in text_file:
    line = line.replace('\n', '')
    elements_text.append(line)
text_file.close()
encrypt_file()

numbers = open('numbers.txt', 'r', encoding='utf-8')
result = 0
for line in numbers:
    for symbol in line:
        if symbol.isdigit():
            result += int(symbol)
numbers.close()

answer = open('answer.txt', 'w', encoding='utf-8')
answer.write(str(result))
answer.close()

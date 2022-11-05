zen_file = open('zen.txt', 'r', encoding='utf-8')
text = []
for line in zen_file:
    line = line.replace('\n', '')
    text.insert(0, line)
zen_file.close()

for line in text:
    print(line)
first_tour = open('first_tour.txt', 'r', encoding='utf-8')
scores = 0
information = []
for line in first_tour:
    line = line.replace('\n', '')
    if line.isdigit():
        scores = int(line)
    else:
        player = line.split()
        information.append(player)
first_tour.close()

for player in information:
    if int(player[2]) <= scores:
        information.remove(player)

second_tour = open('second_tour.txt', 'w', encoding='utf-8')
print("Содержимое файла second_tour.txt:")
second_tour.write(''.join([str(len(information)), '\n']))
print(len(information))
information.sort(key=lambda person: person[2], reverse=True)
for index, player in enumerate(information):
    correct_player = "{}) {}. {} {}".format(index + 1, player[1][0], player[0], player[2])
    second_tour.write(''.join([correct_player, '\n']))
    print(correct_player)

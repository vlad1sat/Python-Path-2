name_user = input("Введите свой никнейм: ")

with open('chat.txt', 'a', encoding='utf-8') as chat:
    while True:
        command = input("\nВведите команду!\n1. Посмотреть текущий текст чата.\n2. Отправить сообщение.\n")
        if command == 1:
            print(chat)

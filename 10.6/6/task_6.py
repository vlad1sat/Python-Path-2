name_user = input("Введите свой никнейм: ")

while True:
    try:
        command = int(
            input("\nВведите команду!\n1. Посмотреть текущий текст чата.\n2. Отправить сообщение.\n3. Выход.\n"))
    except ValueError:
        print("Неверно введенная команда!")
    else:
        if command == 1:
            with open('chat.txt', 'r', encoding='utf-8') as show_chat:
                for chat_message in show_chat:
                    print(chat_message, end='')
        elif command == 2:
            with open('chat.txt', 'a', encoding='utf-8') as add_chat:
                message = input("Введите сообщение: ")
                add_chat.write(''.join([name_user, ': ', message, '\n']))
        elif command == 3:
            print("Выход из чата!")
            break

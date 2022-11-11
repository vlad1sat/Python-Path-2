import random

import game_21 as game


def gameplay(player: game.Player):
    print("\nПриветствуем тебя {} в игре 21!".format(player.name))
    while True:
        score = player.get_sum_cards()
        print("Ваши карты: ", player.show_cards())
        print("Сумма твоих карт: {}".format(score))
        command = input("Хочешь взять еще карту? ").lower()
        if command == "да":
            player.take_card()
        else:
            dealer_score = random.randint(15, 24)
            if dealer_score < score <= 21 or dealer_score > 21 >= score:
                print("\nВы выиграли дилера!\n")
            elif dealer_score > 21 and score > 21:
                print("\nВы перебрали карт с диллером!\n")
            elif dealer_score == score:
                print("\nНичья!\n")
            else:
                print("\nДилер обыграл вас!\n")
            print("Сумма твоих карт: {}. Сумма карт диллера: {}".format(score, dealer_score))
            print("Ваши карты: ", player.show_cards())
            break


name = input("Введите свое имя: ")
user_player = game.Player(name, game.Deck())
gameplay(user_player)

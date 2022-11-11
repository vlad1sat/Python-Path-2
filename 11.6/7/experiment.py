import random
from person import Person


def play(person: Person):
    for day in range(1, 366):
        print("День {}. Игрок: {}".format(day, person.name))
        command = random.randint(1, 6)
        if person.satiety < 20:
            person.eat_food()
        elif person.food < 10:
            person.go_store()
            continue
        elif person.money < 50:
            person.work()
            continue
        elif command == 1:
            person.work()
        elif command == 2:
            person.eat_food()
        else:
            person.play()
        if person.is_died:
            print("День {}. Игрок {} умер!".format(day, person.name))
            break


first_person = Person("Миша")
second_person = Person("Гриша")
play(first_person)
play(second_person)


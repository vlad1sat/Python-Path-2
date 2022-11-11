from warrior import Warrior


first_warrior = Warrior("1")
second_warrior = Warrior("2")
first_warrior.hit(second_warrior)
while True:
    second_warrior.hit(first_warrior)
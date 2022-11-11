class Person:

    def __init__(self, name):
        self.name = name
        self.food = 50
        self.money = 0
        self.satiety = 50
        self.is_died = False

    def eat_food(self):
        if self.food < 15:
            self.is_died = True
            return
        self.food -= 15
        self.satiety = 100 if self.satiety + 20 >= 100 else + 20

    def work(self):
        if self.satiety < 15:
            self.is_died = True
            return
        self.satiety -= 15
        self.money += 50

    def play(self):
        if self.satiety < 15:
            self.is_died = True
            return
        self.satiety -= 15

    def go_store(self):
        if self.money < 30:
            return
        self.money -= 30
        self.food += 15



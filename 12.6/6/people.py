import random


class House:
    food = 50
    money = 100
    cat_food = 30
    dirt = 0


class Resident:
    def __init__(self, name, satiety, happiness):
        self.name = name
        self.satiety = satiety
        self.happiness = happiness

    def eat(self):
        self.satiety += 30
        House.food -= 30
        print(f'{self.name} ест')


class Husband(Resident):
    def __init__(self, name, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness)
        self.work = 150

    def work_day(self):
        House.money += self.work
        self.satiety -= 10
        print(f'Муж идет на работу, деньги {House.money}')

    def game(self):
        self.happiness += 20
        self.satiety -= 10
        print('Муж играет')

    def pretting_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print('Муж гладит кота')

    def __str__(self):
        return f'{self.name}'


class Wife(Resident):
    def __init__(self, name, satiety=30, happiness=100):
        super().__init__(name, satiety, happiness)

    def buy_food(self):
        self.satiety -= 10
        House.food += 100
        House.money -= 100
        print(f'Жена идет в магазин, еда {House.food} деньги {House.money}')

    def buy_cat_food(self):
        self.satiety -= 10
        House.cat_food += 50
        House.money -= 50
        print(f'Жена покупает еду коту, еда кота {House.cat_food} деньги {House.money}')

    def pretting_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print('Жена Гладит кота')

    def purchase(self):
        House.money -= 350
        self.happiness += 60
        self.satiety -= 10
        print(f'Жена покупает шубу, деньги {House.money}')

    def cleaning(self):
        House.dirt -= 10
        self.satiety -= 10

    def __str__(self):
        return f'{self.name}'


class Cat(Resident):
    def __init__(self, name, satiety=30):
        super().__init__(name, satiety, happiness=100)

    def eat(self):
        self.satiety += 20
        House.cat_food -= 10
        print('Кот ест ')

    def slip(self):
        self.satiety -= 10
        return f'Кот спит'

    def shitting(self):
        self.satiety -= 10
        House.dirt += 5
        print(f'Кот подрал обои')

    def __str__(self):
        return f'{self.name}'


husband = Husband(name='Гриша')
wife = Wife(name='Лола')
cat = Cat('Лакки')

for day in range(1, 366):
    print('День {}'.format(day))
    House.dirt += 5

    person = random.choice([husband, wife, cat])

    if person.satiety <= 0:
        print(f'К сожалению, {person.name} помер с голоду ')
        break
    if person.happiness <= 10 and not isinstance(person, Cat):
        print(f'К сожалению, {person.name} умер от депрессии ')
        break

    if isinstance(cat, Cat) and House.cat_food >= 20:
        cat.eat()
    elif isinstance(cat, Cat):
        if random.randint(1, 2) == 1:
            cat.shitting()
        else:
            print('Кот спит')

    if House.dirt >= 90:
        wife.happiness -= 10
        husband.happiness -= 10

    if isinstance(husband, Husband):
        if House.money <= 150:
            husband.work_day()
        elif husband.happiness <= 50:
            husband.game()
        elif husband.happiness <= 40:
            husband.pretting_cat()
        elif House.food >= 30:
            husband.eat()

    if isinstance(wife, Wife):
        if House.food <= 60 and House.money >= 100:
            wife.buy_food()
        elif House.cat_food <= 20:
            wife.buy_cat_food()

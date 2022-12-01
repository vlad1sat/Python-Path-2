import random


class House:
    food = 50
    money = 100
    cat_food = 30
    dirt = 0


class Person:
    def __init__(self, name):
        self.__name = name
        self.satiety = 30
        self.happiness = 100

    @property
    def name(self):
        return self.__name

    def eat(self):
        count_eat_food = 0
        while House.food <= 0 or count_eat_food == 0:
            self.satiety += 1
            count_eat_food += 1
            House.food -= 1
        print('{} ест'.format(self.name))


class RelaxWithCat(Person):

    def prettying_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print('{} гладит кота'.format(self.name))


class Husband(RelaxWithCat):
    def __init__(self, name):
        super().__init__(name)
        self.work = 150

    def work_day(self):
        House.money += self.work
        self.satiety -= 10
        print('Муж идет на работу, деньги {}'.format(House.money))

    def game(self):
        self.happiness += 20
        self.satiety -= 10
        print('Муж играет')


class Wife(Person):

    def buy_food(self):
        self.satiety -= 10
        House.food += 100
        House.money -= 100
        print('Жена идет в магазин, еда {0} деньги {1}'.format(House.food, House.money))

    def buy_cat_food(self):
        self.satiety -= 10
        House.cat_food += 50
        House.money -= 50
        print('Жена покупает еду коту, еда кота {0} деньги {1}'.format(House.cat_food, House.money))

    def purchase(self):
        House.money -= 350
        self.happiness += 60
        self.satiety -= 10
        print('Жена покупает шубу, деньги {}'.format(House.money))

    def cleaning(self):
        House.dirt -= 10
        self.satiety -= 10


class Cat(Person):

    def eat(self):
        self.satiety += 20
        House.cat_food -= 10
        print('Кот ест')

    def sleep(self):
        self.satiety -= 10
        print('Кот спит')

    def shitting(self):
        self.satiety -= 10
        House.dirt += 5
        print('Кот подрал обои')


husband = Husband('Гриша')
wife = Wife('Лола')
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

    if isinstance(cat, Cat):
        if House.cat_food >= 20:
            cat.eat()
        else:
            if random.randint(1, 2) == 1:
                cat.shitting()
            else:
                cat.sleep()

    if House.dirt >= 90:
        wife.happiness -= 10
        husband.happiness -= 10

    if isinstance(husband, Husband):
        if House.money <= 150:
            husband.work_day()
        elif husband.happiness <= 50:
            husband.game()
        elif husband.happiness <= 40:
            husband.prettying_cat()
        elif House.food >= 30:
            husband.eat()

    if isinstance(wife, Wife):
        if House.food <= 60 and House.money >= 100:
            wife.buy_food()
        elif House.cat_food <= 20:
            wife.buy_cat_food()

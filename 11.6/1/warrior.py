class Warrior:
    def __init__(self, name: str):
        self.health = 100
        self.name = name

    def hit(self, unit):
        if isinstance(unit, Warrior):
            unit.health -= 20
            print("Боец {} ударил бойца {}.".format(self.name, unit.name))
            if unit.health <= 0:
                print('Боец {} погиб.'.format(unit.name))
                exit()
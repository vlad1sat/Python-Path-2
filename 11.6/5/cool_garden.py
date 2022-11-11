class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        return self.state == 3

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка проростает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if not i_potato.is_ripe():
                print('Картошка ещё не созрела!\n')
                break
            else:
                print('Вся картошка созрела! Можно собирать!\n')


class Farmer:

    def __init__(self, name, plant_species):
        self.name = name
        self.plant_species = plant_species

    def grow_plants(self):
        for plant in self.plant_species.potatoes:
            plant.grow()

    def collect_plants(self, count_plants):
        collect_plants = 0
        for plant in self.plant_species.potatoes:
            if plant.is_ripe():
                collect_plants += 1
                plant.state = 0
            if count_plants == collect_plants:
                print('Растения собраны!')
                break
        else:
            print('Созрело мало растений! Собрано: {}'.format(collect_plants))

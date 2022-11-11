class Water:
    name = 'Вода'

    def __add__(self, element):
        if isinstance(element, Burn):
            return Dust()
        elif isinstance(element, Earth):
            return Dirt()
        elif isinstance(element, Air):
            return Storm()
        return None

    def __str__(self):
        return self.name


class Air:
    name = "Воздух"

    def info_print(self):
        print(self.name)

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Burn):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        return None

    def __str__(self):
        return self.name


class Burn:
    name = "Огонь"

    def info_print(self):
        print(self.name)

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        return None

    def __str__(self):
        return self.name

class Earth:
    name = "Земля"

    def info_print(self):
        print(self.name)

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Burn):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        return None

    def __str__(self):
        return self.name


class Steam:
    name = "Пар"

    def __str__(self):
        return self.name


class Dirt:
    name = "Грязь"

    def __str__(self):
        return self.name


class Lightning:
    name = "Молния"

    def __str__(self):
        return self.name


class Dust:
    name = "Пыль"

    def __str__(self):
        return self.name


class Storm:
    name = "Шторм"

    def __str__(self):
        return self.name


class Lava:
    name = "Лава"

    def __str__(self):
        return self.name

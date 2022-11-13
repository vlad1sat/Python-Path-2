class Property:

    def __init__(self, worth: float):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def create_tax(self):
        return 0


class Apartment(Property):

    def __init__(self, worth: float):
        super().__init__(worth)
        self.__tax = self.create_tax()

    def get_tax(self):
        return self.__tax

    def create_tax(self):
        return round(self.get_worth() / 1000, 2)


class Car(Property):

    def __init__(self, worth: float):
        super().__init__(worth)
        self.__tax = self.create_tax()

    def get_tax(self):
        return self.__tax

    def create_tax(self):
        return round(self.get_worth() / 200, 2)


class CountryHouse(Property):

    def __init__(self, worth: float):
        super().__init__(worth)
        self.__tax = self.create_tax()

    def get_tax(self):
        return self.__tax

    def create_tax(self):
        return round(self.get_worth() / 500, 2)

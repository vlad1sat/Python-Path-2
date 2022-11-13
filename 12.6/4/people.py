class Person:

    def __init__(self, name: str, surname: str, age: int):
        self.__name = name
        self.__surname = surname
        self._age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__surname


class Employer(Person):

    def get_salary(self):
        pass


class Manager(Employer):

    def get_salary(self):
        return 13000


class Agent(Employer):

    def __init__(self, name: str, surname: str, age: int, volume_sales: float):
        super().__init__(name, surname, age)
        self.__volume_sales = volume_sales

    def get_salary(self):
        return 5000 * self.__volume_sales * 0.05


class Worker(Employer):

    def __init__(self, name: str, surname: str, age: int, work_hours: int):
        super().__init__(name, surname, age)
        self.__work_hours = work_hours

    def get_salary(self):
        return 100 * self.__work_hours

import math


class Car:

    def __init__(self, coordinate_x, coordinate_y, angle):
        self.__coordinate_x = coordinate_x
        self._coordinate_y = coordinate_y
        self.__angle = angle

    def move(self, distance):
        self.__coordinate_x = self.__coordinate_x + distance * math.cos(self.__angle)
        self._coordinate_y = self.__coordinate_x + distance * math.sin(self.__angle)

    def turn(self, turn_angle):
        self.__angle += turn_angle


class Bus(Car):
    COUNT_DISTANCE = 8
    COEFFICIENT_PEOPLE = 0.5

    def __init__(self, coordinate_x, coordinate_y, angle, count_people):
        super().__init__(coordinate_x, coordinate_y, angle)
        self.__count_people = count_people
        self.__money = 0

    def enter(self, count_enter_people):
        self.__count_people += count_enter_people

    def exit(self, count_exit_people):
        if not self.__count_people > count_exit_people:
            self.__count_people -= count_exit_people
        else:
            print("Людей меньше в автобусе!")

    def move(self, distance):
        super().move(distance)
        self.__money += distance * Bus.COUNT_DISTANCE + self.__count_people * Bus.COEFFICIENT_PEOPLE

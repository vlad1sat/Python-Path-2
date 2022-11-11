import math


class Circle:

    def __init__(self, radius: float, coordinate_x: float = 0, coordinate_y: float = 0):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.radius = radius

    def der_square(self):
        return round(math.pi * self.radius ** 2, 2)

    def get_perimeter(self):
        return round(math.pi * 2 * self.radius, 2)

    def increase_circle(self, magnifier: float):
        self.radius *= magnifier

    def is_intersection(self, circle):
        if isinstance(circle, Circle):
            if self.coordinate_x == circle.coordinate_x:
                if self.radius + circle.radius > abs(self.coordinate_y - circle.coordinate_y):
                    print('Окружности пересекаются')
                else:
                    print('Окружности не пересекаются')
            elif self.coordinate_y == circle.coordinate_y:
                if self.radius + circle.radius > abs(self.coordinate_x - circle.coordinate_x):
                    print('Окружности пересекаются')
                else:
                    print('Окружности не пересекаются')
            elif (self.radius + circle.radius) ** 2 > abs((self.coordinate_x - circle.coordinate_x) ** 2 -
                                                            (self.coordinate_y - circle.coordinate_y) ** 2):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')


first_circle = Circle(2)
second_radius = Circle(1, 1, 1)

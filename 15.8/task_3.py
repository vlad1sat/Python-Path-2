from math import sqrt
from abc import ABC
from typing import List, Any


class Figure(ABC):

    def get_square(self) -> float:
        pass

    def get_perimeter(self) -> float:
        pass


class Square(Figure):

    def __init__(self, side_square: float) -> None:
        self.__side_square = side_square

    @property
    def side_square(self) -> float:
        return self.__side_square

    def get_square(self) -> float:
        return self.__side_square ** 2

    def get_perimeter(self) -> float:
        return 4 * self.__side_square


class Triangle(Figure):

    def __init__(self, height_triangle: float, side_triangle: float) -> None:
        self.__height_triangle = height_triangle
        self.__side_triangle = side_triangle

    @property
    def height_triangle(self) -> float:
        return self.__height_triangle

    @property
    def side_triangle(self) -> float:
        return self.__side_triangle

    def get_square(self) -> float:
        return 0.5 * self.__height_triangle * self.__side_triangle

    def get_perimeter(self) -> float:
        return self.__side_triangle + 2 * sqrt(self.__height_triangle ** 2 + self.__side_triangle ** 2)


class Cube(Square):

    def __init__(self, side_square: float) -> None:
        super().__init__(side_square)
        self.__figure = [Square(side_square) for _ in range(6)]

    def get_square(self) -> float:
        square = 0
        for base_cube in self.__figure:
            square += base_cube.get_square()
        return square

    def get_perimeter(self) -> float:
        perimeter = 0
        for base_cube in self.__figure:
            perimeter += base_cube.get_perimeter()
        return perimeter


class Pyramid(Triangle, Square):

    def __init__(self, height_triangle: float, side_triangle: float, side_square: float, count_triangle):
        super().__init__(height_triangle, side_triangle)
        self.__side_square = side_square
        self.__count_triangle = count_triangle
        self.figure = self.__get_figure()

    def __get_figure(self) -> List[Any]:
        figure = []
        for _ in range(self.__count_triangle):
            figure.append(Triangle(height_triangle=self.height_triangle, side_triangle=self.side_triangle))
        figure.append(Cube(self.__side_square))
        return figure

    def get_square(self) -> float:
        square = 0
        for base_cube in self.figure:
            square += base_cube.get_square()
        return square


cube = Cube(5)
print(cube.get_square())
pir = Pyramid(5, 10, 10, 4)
print(pir.get_square())

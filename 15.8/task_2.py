from abc import ABC
from math import pi


class MyMath(ABC):

    @classmethod
    def circle_len(cls, radius: float) -> float:
        return 2 * pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        return pi * radius ** 2

    @classmethod
    def volume_cube(cls, side: float) -> float:
        return side ** 3

    @classmethod
    def volume_sphere(cls, radius: float) -> float:
        return 4 * pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
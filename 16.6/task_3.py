from time import time
from datetime import datetime
import functools
from typing import Callable, Any


def timer(cls, func: Callable, date_format: str) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        correct_format = date_format
        for element in correct_format:
            if element.isalpha():
                correct_format = correct_format.replace(element, '%' + element)

        print("Запускается '{}.{}'. Дата и время запуска: {}"
              .format(cls.__name__, func.__name__, datetime.now().strftime(correct_format)))
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print("Завершение '{}.{}', время работы = {} сек.".format(cls.__name__, func.__name__, round(end - start, 3)))
        return result
    return wrapper


def log_methods(date_format: str) -> Callable:
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                current_method = getattr(cls, method)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, method, decorated_method)
        return cls
    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
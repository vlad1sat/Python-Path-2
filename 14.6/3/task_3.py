from typing import Callable, Any
import functools
from datetime import datetime


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            result = func(*args, **kwargs)
            print('Название функции: {}. Её документация: {}.'.format(func.__name__, func.__doc__ if func.__doc__ is not None else '-'))
            return result
        except Exception as error:
            with open('function_errors.log', 'a', encoding='utf-8') as errors:
                errors.write('Название некорректно работаюшей функции: {}. Ошибка: {}. Время возникновение ошибки: {}\n'
                             .format(func.__name__, error, datetime.now()))
    return wrapped_func


@logging
def get_lazy_numbers():
    for number in range(10):
        yield number


@logging
def broke_func():
    return 2 / 0

@logging
def broke_func_2():
    return 2 / 'rarara'


broke_func()
for num in get_lazy_numbers():
    print(num)
broke_func_2()

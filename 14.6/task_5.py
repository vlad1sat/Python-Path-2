from typing import Callable, Any
from functools import wraps


def counter(func: Callable) -> Callable:
    wraps(func)

    def wrapper(*args, **kwargs) -> Any:
        wrapper.count += 1
        print('{} была вызвана: {}x'.format(func.__name__, wrapper.count))
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def hi():
    print('Hi')


@counter
def bye():
    print('Bye')


hi()
hi()
bye()

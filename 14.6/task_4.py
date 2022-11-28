from typing import Callable, Any
from functools import wraps


def debug(func: Callable) -> Callable:
    wraps(func)

    def wrapped_func(*args, **kwargs) -> Any:
        print('Вызывается {}({})'.format(func.__name__, ", ".join(
                list(f"\"{arg}\""
                     if isinstance(arg, str) else
                     str(arg) for arg in args)
                +
                list(f"{k}=\"{v}\""
                     if isinstance(v, str) else
                     f"{k}={v}" for k, v in kwargs.items())
            )))
        result = func(*args, **kwargs)
        print('\'{}\' вернула значение \'{}\''.format(func.__name__, result))
        return result
    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


@debug
def test(a, b):
    return a + b


test(2, 3)
greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

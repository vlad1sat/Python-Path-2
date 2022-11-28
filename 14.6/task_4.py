from typing import Callable, Any
import functools


def debug(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print('Вызывается {}({})'.format(func.__name__, ", ".join(
                list(f"\"{arg}\""
                     if isinstance(arg, str) else
                     str(arg) for arg in args)
                +
                list(f"{key}=\"{value}\""
                     if isinstance(value, str) else
                     f"{key}={value}" for key, value in kwargs.items())
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

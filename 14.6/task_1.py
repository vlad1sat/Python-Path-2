from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_funct(*args, **kwargs) -> Any:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func(*args, **kwargs)
    return wrapped_funct


@how_are_you
def test():
    print('<Тут что-то происходит...>')


@how_are_you
def get_lazy_numbers():
    for number in range(10):
        yield number


test()
for num in get_lazy_numbers():
    print(num)

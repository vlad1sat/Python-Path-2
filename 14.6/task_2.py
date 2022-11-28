from typing import Callable, Any
from functools import wraps
from time import sleep


def wait_time(seconds: int) -> Callable:
    def wait(func: Callable) -> Callable:
        wraps(func)

        def wrapped_func(*args, **kwargs) -> Any:
            sleep(seconds)
            return func(*args, **kwargs)
        return wrapped_func
    return wait


@wait_time(5)
def get_lazy_numbers():
    for number in range(10):
        yield number


for num in get_lazy_numbers():
    print(num)

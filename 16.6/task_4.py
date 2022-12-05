import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable):
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print("Переданные арги и кварги:", dec_args, dec_kwargs)
        return func(*func_args, **func_kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

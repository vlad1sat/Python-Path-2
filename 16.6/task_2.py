import functools
from typing import Callable, Optional, Any

app = dict()


def callback(_func: Optional[Callable] = None, *, base_route: str = None) -> Callable:
    def call(func: Callable) -> Callable:
        app[base_route] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            func_call = func(*args, **kwargs)
            return func_call
        return wrapper

    if _func is None:
        return call
    return call(_func)


@callback(base_route='//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

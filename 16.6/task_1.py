import functools
from typing import Callable, Any

user_permissions = ['admin']


def check_permission(key: str) -> Callable:
    def check(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            try:
                if key not in user_permissions:
                    raise PermissionError
                else:
                    return func(*args, **kwargs)
            except PermissionError:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
        return wrapped_func
    return check


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
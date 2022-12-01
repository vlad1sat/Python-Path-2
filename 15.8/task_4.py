from abc import ABC


class Date(ABC):

    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.__day = day
        self.__month = month
        self.__year = year

    @classmethod
    def from_string(cls, user_date: str) -> 'Date':
        day, month, year = map(int, user_date.split('-'))
        return cls(day, month, year)

    @classmethod
    def is_date_valid(cls, user_date: str) -> bool:
        day, month, year = map(int, user_date.split('-'))
        if 1 <= day <= 31 and 1 <= month <= 31 and 0 <= year <= 9999:
            return True
        return False

    def __str__(self):
        return 'День: {} \tМесяц: {} \tГод: {}'.format(self.__day, self.__month, self.__year)


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

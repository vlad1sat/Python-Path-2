from abc import ABC


class Date(ABC):
    __date = None

    @classmethod
    def from_string(cls, user_date: str):
        cls.__date = cls.data_processing(user_date)
        return 'День:{} \tМесяц:{} \tГод:{}'.format(cls.__date[0], cls.__date[1], cls.__date[2])

    @classmethod
    def is_date_valid(cls, user_date: str) -> bool:
        format_date = cls.data_processing(user_date)
        for index in range(3):
            if format_date[index] != cls.__date[index]:
                return False
        return True

    @classmethod
    def data_processing(cls, user_data: str):
        format_date = [int(element) for element in user_data.split('-')]
        if len(format_date) == 3 and 1 <= format_date[0] <= 99 and 1 <= format_date[1] <= 99 and 1000 <= format_date[2] <= 9999:
            return format_date
        else:
            raise TypeError


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

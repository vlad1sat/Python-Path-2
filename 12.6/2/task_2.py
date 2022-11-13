from random import randint

CARMA = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    count_carma = 0
    with open('exceptions.log', 'w', encoding='utf-8') as exceptions:
        while True:
            count_carma += randint(1, 7)
            rand_except = randint(1, 10)
            if rand_except == 5:
                try:
                    choose_exception = randint(1, 6)
                    if choose_exception == 1:
                        raise IamGodError()
                    elif choose_exception == 2:
                        raise DrunkError()
                    elif choose_exception == 3:
                        raise CarCrashError()
                    elif choose_exception == 4:
                        raise GluttonyError()
                    elif choose_exception == 5:
                        raise DepressionError()
                    else:
                        raise SuicideError()
                except IamGodError:
                    exceptions.write(''.join(['IamGodError', '\n']))
                except DrunkError:
                    exceptions.write(''.join(['IamGodError', '\n']))
                except CarCrashError:
                    exceptions.write(''.join(['CarCrashError', '\n']))
                except GluttonyError:
                    exceptions.write(''.join(['GluttonyError', '\n']))
                except DepressionError:
                    exceptions.write(''.join(['DepressionError', '\n']))
                except SuicideError:
                    exceptions.write(''.join(['SuicideError', '\n']))
            if count_carma >= CARMA:
                print('WIN')
                break


one_day()
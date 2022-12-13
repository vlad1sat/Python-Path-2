import re
from typing import List

correct_symbols = re.findall(r'\w+', 'А, В, Е, К, М, Н, О, Р, С, Т, У, Х.')

if __name__ == '__main__':
    numbers: str = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
    all_numbers: List[str] = re.findall(r'\w+', numbers)
    auto_numbers: List[str] = [number for number in all_numbers if re.fullmatch(
        r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', number)]
    taxi_numbers: List[str] = [number for number in all_numbers if re.fullmatch(r'[АВЕКМНОРСТУХ]{2}\d{5,6}', number)]
    print('Список номеров частных автомобилей:', auto_numbers)
    print('Список номеров такси:', taxi_numbers)


import re
from typing import List

numbers: List[str] = ['9999999999', '999999-999', '99999x9999', '5555555555', '8675940306', '89rrrrrrrr']
if __name__ == '__main__':
    correct_numbers: List[str] = [number for number in numbers if re.fullmatch(r'[89][0123456789]{9}', number)]
    print(correct_numbers)

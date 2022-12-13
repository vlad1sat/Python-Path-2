import re
from typing import List

text: str = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""
if __name__ == '__main__':
    all_words: List[str] = re.findall(r'\w+', text)
    result: List[str] = list(filter(lambda word: len(word) == 4, all_words))
    print(result)
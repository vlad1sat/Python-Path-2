from typing import List
import requests
from re import findall

if __name__ == '__main__':
    my_request: str = requests.get('http://www.columbia.edu/~fdc/sample.html').text
    all_h3: List[str] = findall(r'>.+</h3>', my_request)
    result: List[str] = list(map(lambda x: x[1:-5], all_h3))
    print(result)
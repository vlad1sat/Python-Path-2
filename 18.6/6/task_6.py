import json
from typing import Any, List


def add_information(data: dict, goal: str) -> Any:
    if goal in data:
        return data[goal]
    for key, value in data.items():
        if isinstance(value, dict):
            item = add_information(value, goal)
            if item is not None:
                return item


def find_differences(first_data: dict, second_data: dict) -> bool:
    first_values: list = list(first_data.values())
    second_values: list = list(second_data.values())
    for index, first_value in enumerate(first_values):
        if first_value != second_values[index]:
            return True
    return False


if __name__ == '__main__':
    diff_list: List[str] = ['services', 'staff', 'datetime']
    result = dict()
    data_old, data_new = dict(), dict()

    with open('json_old.json', 'r', encoding='utf-8') as json_old:
        data_old = json.load(json_old)
    with open('json_new.json', 'r', encoding='utf-8') as json_new:
        data_new = json.load(json_new)

    for diff_element in diff_list:
        data_1: Any = add_information(data_old, diff_element)
        data_2: Any = add_information(data_new, diff_element)
        if isinstance(data_1, list):
            if find_differences(data_1[0], data_2[0]):
                result[diff_element] = data_2
        elif isinstance(data_1, dict):
            if find_differences(data_1, data_2):
                result[diff_element] = data_2
        else:
            if data_1 != data_2:
                result[diff_element] = data_2

    with open('result.json', 'w', encoding='utf-8') as result_file:
        json.dump(result, result_file, indent=4)

    print(result)

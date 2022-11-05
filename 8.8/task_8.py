def element_list(difficult_list: list):
    result = []
    for element in difficult_list:
        if not isinstance(element, list):
            result.append(element)
        else:
            result.extend(element_list(element))
    return result


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(element_list(nice_list))

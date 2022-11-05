def my_sum(*args):
    sum_elements = 0
    for element in args:
        if not isinstance(element, list):
            sum_elements += element
        else:
            for element_list in element:
                sum_elements += my_sum(element_list)
    return sum_elements


print(my_sum([[1, 2, [3]], [1], 3]))
print(my_sum(1, 2, 3, 4, 5))

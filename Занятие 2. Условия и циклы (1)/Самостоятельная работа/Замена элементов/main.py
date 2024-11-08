list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Поменяйте местами значения согласно условию

ind = 0
max_element = list_numbers[0]


for ind, elem in enumerate(list_numbers):
    current_value = list_numbers[ind]
    if current_value >= max_element:
        max_element = current_value
        max_element_index = ind
# print("Максимальный последний элемент =", max_element, "находится по индексу", max_element_index)
list_numbers[9]=25
list_numbers[-1]=90

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]

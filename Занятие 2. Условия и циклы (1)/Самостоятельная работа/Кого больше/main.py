list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

# TODO завести отдельные счетчики для четных и нечетных чисел
even_count, odd_count = 0, 0
# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных

# TODO вывести каких чисел больше

for num in list_:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
if even_count>odd_count:
    print("Четных чисел больше")
elif even_count<odd_count:
    print("Нечетных чисел больше")
elif even_count == odd_count:
    print("Четных и нечетных одинаковое количество")

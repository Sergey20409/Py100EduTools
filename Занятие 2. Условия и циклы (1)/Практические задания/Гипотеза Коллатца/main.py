num = 27  # Число для проверки гипотезы Коллатца
count = 0  # Количество операций над числом
while num!=1:
    if num % 2 == 0:
        num=num/2
    else:
        num=num*3+1
    count+=1
# TODO Посчитайте количество действий над числом по гипотезе Коллатца

print("Количество действий:", count)

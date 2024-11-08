# TODO Распечатать таблицу умножения
i=1
j=2
print(end='')
for i in range(2, 10):
    while j<=9:
        end = '\n' if j == 9 else ' '
        # if j==9:
        #     end='\n'
        # else:
        #     end = ' '
        print(f"{(i*j):>2}", end=end)
        j+=1
    # print()
    j=2
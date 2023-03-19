# task_23
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randrange

N = int(input("Введите N: "))
array = []
for i in range(N):
    array.append(randrange(1, 20))
print(array)

COUNT = 0
for i in range(1, N):
    if array[i] > array[i-1]:
        COUNT += 1
print(COUNT)

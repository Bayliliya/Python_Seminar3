# Задача_16: Требуется вычислить, сколько раз встречается
# некоторое число X в массиве A[1..N]
# Пользователь в первой строке вводит
#  натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

from random import randrange

N = int(input("Введите N: "))
X = 4
array = []
for i in range(N):
    array.append(randrange(2, 5))
print(array)

COUNT = 0
for i in array:
    if i == X:
        COUNT += 1
print(COUNT)

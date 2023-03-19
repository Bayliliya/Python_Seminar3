# Задача_18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

from random import randint

N = int(input("Введите N: "))
X = int(input("Введите X: "))
array = []
for i in range(N):
    array.append(randint(-10, 10))
print(array)

MIN = float("inf")
MIN_VALUE = 0
for i in array:
    if abs(X - i) <= MIN:
        MIN = abs(X-i)
        MIN_VALUE = i
print(MIN_VALUE)

#  Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

LIST_1 = [2, 4, 8, 8, 3, 5, 2, 4, 3, 3]
LIST_Modify = []
for i in LIST_1:
    if i not in LIST_Modify:
        LIST_Modify.append(i)        
print(LIST_Modify, len(LIST_Modify), sep="//")
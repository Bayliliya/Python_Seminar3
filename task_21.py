# task_21
# Напишите программу для печати всех уникальных значений в словаре.
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII": " S005 "},
# {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит
lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
       {"VII": "S005"}, {" V ": "S009"}, {" VIII ": "S007"}]
unique_key = set()
for dict_lst in lst:
    for value in dict_lst.values():
        unique_key.add(value)
print(unique_key)

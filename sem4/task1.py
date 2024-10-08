'''
Задача №1. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
'''
# 1-й Вариант решения:

# sp = "a a a b c a a d c d d"
# res = ""
# d = {}
# for i in sp:
#     if i != " ":
#         if i in d.keys():
#             d[i] += 1
#             res = res + i + "_" + str(d[i]) + " "
#         else:
#             d[i] = 0
#             res = res + i + " "
            
# print(res)

# - - - - - - - - - - - - - - - - - - - - - - - 
# Второй вариант решения

s = 'a a a b c a a d c d d '

data = s.split()
data_dict = {}
result_str = ''


for elem in data:
    if elem in data_dict.keys():
        data_dict[elem] += 1
        result_str += f'{elem}_{data_dict[elem]} '
    else:
        data_dict[elem] = 0
        result_str += f'{elem} '
        
        
print(result_str)
        

'''
Дан список чисел. 
Определите, сколько в нем встречается различных чисел
input:[1,1,2,0,-1,3,4,4]
output: 6
'''




s = [1,1,2,0,-1,3,4,4]
s = set(s) # Список превратим во множество, остануться только уникальные переменные
print(f"Output: {len(s)}") # Найдем длину множества

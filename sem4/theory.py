'''
Библеотеки
Это питоновский код написанный ранее, которым можно пользоваться
Есть встроенные в питон
Некоторые устанавливаются отдельно
'''
# Добавление библеотек

import random # Импортируем модуль Рандом
# import random as rnd # Модуль можно переименовать для удобства обращения

# Создадим простой код который будет заполнять список случайными целыми значениями

lst = [] # Создали пустой список
for _ in range(10): # Используем анонимную переменную  "_"
    lst.append(random.randint(1, 100)) # получим случайное целое число от 1 до 100 включительно
print(lst)

# Другой вариант

from random import randint # Импортируем из модуля random  ф-ю randint(есть риск конфликта имен в большом коде)



lst = []
for _ in range(10):
    lst.append(randint(1,100))
print(lst)


# Добавим ф-ю. 
import random as rnd



# Ф-ю Принято выделать на верх программного кода после блока импорта
# Написание ф-ии начинаем с def (в названии ф-ии рек-ся вначале использовать глагол)
def create_rnd_list(size): # Создаем ф-ю create_rnd_list На входе добавляем переменную size
    lst = [] # Создали пустой список
    for _ in range(size):
        lst.append(rnd.randint(1, 100)) # Создает случайное целое число от 1 до 100
    return lst # Возвращаем значение lst(Возвращает инф-ю в тело основного кода)


# def puus_two_values(v1, v2) # Создаем ф-ю сложения двух значений
def plus_two_values(v1: int, v2: int) -> int: # Создаем ф-ю и используем анатицию типов данных 
    
    '''
    Напишем справку по этой функции, пр:
    this function add two integer values
    '''
    if isinstance(v1, int) and isinstance(v2, int): # Проверяет являются ли переменные типа int
        return v1 + v2
    else:
        print("Error!") # Если переменные не типа int выводим Error!


# Либо:


    if not (isinstance(v1, int) and isinstance(v2, int)):
        raise TypeError("Must be int values") # Если хотябы одна перменная не int генерируем ошибку "Must be int values"
    return v1 + v2




# Тело основного кода принято писать ниже ф-ии на 4 строчки для лучшей читаемости
# print(create_rnd_list(8))
# print(plus_two_values.__doc__) # Распечатываем справку по ф-ии (метод "Дандер" .__doc__)
# print(plus_two_values(5,8)) # Выведем работу ф-ии со значениями (5, 8)
print(plus_two_values(5,8))

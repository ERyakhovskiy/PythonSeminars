'''
Задача 1 НЕГАФИБОНАЧЧИ по желанию

Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

для k = 9 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]​


Задача 2 Последовательность необязательная

Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
Одно число - это не последовательность.

Пример:

[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7

[1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8

[1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8


Задача 3 Спираль необязательная

Выведите таблицу размером n×n, заполненную числами от 1 до n**2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):


1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9



Задача XO необязательная

Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
Конечно, бот не должен ходить на занятые поля
Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
После каждого хода на экран должна выводиться текущая обстановка на поле.
Например,

| | Х |
| | O |
| | O |

При ходе пользователя у надо спрашивать номер строки и столбца, куда он хочет сделать ход
'''
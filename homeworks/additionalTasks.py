'''
Семминар № 2 !!!!!!
____________________________________________________________________

Допзадачи от меня:

Допзадание 1 - Пользователь вводит любое число (дробное или целое), 
надо посчитать количество цифр в числе. Решаем строго математически,
обращаться к числу как к строке нельзя.

0 -> 1
9 -> 1
56.77 -> 4
-0.0001 - > 5
100.18006 ->8

'''
#  Решение:

num = float(input('Введите число: '))
count = 0
if num >= 1:
    while num > 0:
    
        x = num  % 10
        count += 1
        num = num  // 10
# else:# num < 1:

    # while num < 10 :
    #   if num 
    #     count = 1
    #     y = num * 10
    #     count += 1
 
 
print('Цифр:', count)


'''
Допзадание 2

Валентина прогуляла лекцию по математике.
Преподаватель решил подшутить над нерадивой студенткой и
попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
Для несложных примеров студентка быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.
•
Решить такое вручную, как вы понимаете, практически нереально.
Вот Валентина и обратилась к вам за помощью.
Помогите ей.
Постарайтесь найти самое оптимальное решение.
Результат представьте в виде списка (не забудьте отсортировать по возрастанию).
'''

# Решение:





'''
Семминар № 3!!!!!!
_____________________________________________________________________________________
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








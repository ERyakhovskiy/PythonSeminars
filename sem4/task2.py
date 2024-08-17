'''
Задача №2. Решение в группах
Пользователь вводит текст(строка). Словом
считается последовательность непробельных
символов идущих подряд, слова разделены одним
или большим числом пробелов. Определите, сколько
различных слов содержится в этом тексте.

Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13
'''

# Сначала переведем все в один регистр
# Потом заменим точку на пробел через replace
# Потом делаем .split 
# Потом переводим во множество
# Потом берем длинну этого множества



data = '''She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells'''

data = data.lower().replace(__old: '.', __new: ' ').split()

result = len(set(data))



print(result)
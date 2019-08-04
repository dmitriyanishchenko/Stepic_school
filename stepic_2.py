"""
Сколько итераций цикла будет выполнено в этом фрагменте программы?
"""
# i = 0
# count = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
#     count += 1
# print(count) # count равен 9


"""
Нарисовать треугольник из звездочек(*), приняв количество через ввод (ваприант через умножение строк)
"""
# n = int(input())
# c = 1
# while c <= n:
#     print('*' * c)
#     c += 1

"""
Нарисовать треугольник из звездочек(*), приняв количество через ввод (вариант через сложение строк)
"""
# n = int(input())
# stars = '*'
# while len(stars) <= n:
#     print(stars)
#     stars += '*'


"""
Сколько всего знаков * будет выведено после исполнения фрагмента программы:
"""
# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

"""
Посчитать сумму чисел от a до b
"""
# a = int(input())
# b = int(input())
# s = 0
# i = a
# while i <= b:
#     s += i
#     i += 1
# print(s)


"""
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, 
и после первого введенного нуля выводит сумму полученных на вход чисел.
"""
# a = int(input())
# sum_ = a
# while a != 0:
#     a = int(input())
#     sum_ += a
# print(sum_)


"""
В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования 
достанется большой и вкусный пирог. В команде биологов a человек, а в команде информатиков — b человек.

Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей 
соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. И так как
не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.

Напишите программу, которая помогает найти это число.
Программа должна считывать размеры команд (два положительных целых числа a
и b, каждое число вводится на отдельной строке) и выводить наименьшее число d, которое делится на оба этих числа 
без остатка.
"""
# a = int(input())
# b = int(input())
# d = 1
# while d % a != 0 or d % b != 0:
#     d += 1
# print(d)

# i = 0
# while i < 5:
#     a, b = input().split()
#     a = int(a)
#     b = int(b)
#     if (a == 0) and (b == 0):
#         break
#     if (a == 0) or (b == 0):
#         continue
#     print(a * b)
#     i += 1
#


"""
Определите, какое значение будет иметь переменная i после выполнения следующего фрагмента программы:
"""
# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i) # i =7


"""
Определите, какое значение будет иметь переменная i после выполнения следующего фрагмента программы:
"""
# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)  # i = 10

"""
Напишите программу, которая считывает целые числа с консоли по одному числу в строке.

Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.

"""
# while 1:
#     a = int(input())
#     if a < 10:
#         continue
#     if a > 100:
#         break
#     print(a)

# for i in 2, 3, 5:
#     print(i * i)

# for i in range(10):
#     print(i * i)

# n = int(input())
# for i in range(n):
#     print('*' * n)

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print('*', end='')
#     print()

# lst = [11**11, 1-8, 9e-12, 12, 23, 4, 17, 134,
#        44,
#        55,
#        666,
#        7777,
#        8888,
#        99999
#        ]
# h = [343, 765, 88, 67]
# lst.extend(h)
#
# for idx, val in enumerate(lst):
#     print(f'{idx} : {val}')
# print(f'len lst is {len(lst)}')
# print(f'min value is {min(lst)}')
# print(f'max value is {max(lst)}')
# print(f'sum items is {sum(lst)}')


# lst = [11, 18, 9, 12, 23, 4, 17]
# lost = []
# for idx in range(len(lst)):
#     val = lst[idx]
#     if val > 15:
#         lost.append(val)
#         lst[idx] = 15
# print("modif:", lst, "-lost:", lost)


# lst_sort = sorted(lst)
# print(lst_sort)
# print(type(lst_sort))

# a = "word in spase".split()
# print(a)
# b = int(15.56)
# print(b)
# b = str(b)
# print(b)
"""
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему
 бы очень пригодилась программа, которая показывала бы блок таблицы умножения.

Напишите программу, на вход которой даются четыре числа a
, b, c и d, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех 
чисел отрезка [a;b] на все числа отрезка [c;d] .

Числа a, b, c и d являются натуральными и не превосходят 10, a≤b, c≤d

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. 
Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец 
и строка таблицы
"""
# c, d, a, b = int(input()), int(input()), int(input()), int(input())
#
# if a <= b and c <= d:
#     str_1 = '    '
#     for val in range(a, b + 1):
#         str_1 += str(val)
#         str_1 += '\t'
#     print(str_1)
#     str_2 = ''
#     for i in range(c, d + 1):
#         str_2 = str(i) + '\t'
#         for j in range(a, b + 1):
#             str_2 += str(i * j) + '\t'
#         print(str_2)
# else:
#     print('Invalid input')
"""
Вывести сумму всех целых  нечетных чисел  от a до b, включая обе границы
"""
# a, b = input().split() # Вариант 1
# a = int(a)
# b = int(b)
# s = 0
# for elem in range(a, b + 1):
#     if elem % 2 == 1:# проверка на нечетность внутри цикла
#         s += elem
# print(s)


# a, b = input().split()  # Вариант 2
# a = int(a)
# b = int(b)
# s = 0
# if a % 2 == 0: # если начальный элемент четный,
#     a += 1 # то  добавляем к нему единицу
# for elem in range(a, b + 1, 2): # в цикле идем только по нечетным элементам
#     s += elem # и суммируем
# print(s)


# # Вариант 3
# a, b = (int(i) for i in input().split())  # при вводе используем функцию List Comprehension
# s = 0
# if a % 2 == 0:
#     a += 1
# for elem in range(a, b + 1, 2):
#     s += elem
# print(s)

"""
Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль среднее
арифметическое всех чисел из отрезка [a;b], которые делятся на 3.
В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12]. Всего чисел, делящихся на 3,
на этом отрезке 6: −3,0,3,6,9,12. Их среднее арифметическое равно 4.5
На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3.﻿
"""
a, b = (int(i) for i in input().split())
s = 0
count = 0
for elem in range(a, b + 1):
    if elem % 3 == 0:
        s += elem
        count += 1
res = s / count
print(res)

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
import random

# number = input("Введите вещественное число: ")
# res = 0
# for i in number:
#     res += int(i)
# print(f'Сумма цифр числа {number} = {res}')

# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.

# number = int(input('Введите  количество элементов: '))
# my_list = []
# res = 0
# for i in range(1, number + 1):
#     my_list.append(((1 + 1 / i) ** i))
#     res += (1 + 1 / i) ** i
# print(*my_list, sep= ', ')
# print(f' Сумма элементов = {round(res, 3)}')

# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#
# my_list1 = []
# num = 0
# while num < len(my_list):
#     a = random.choice(my_list)
#     if a not in my_list1:
#         num += 1
#         my_list1.append(a)
# else:
#     num
# print(my_list)
# print(my_list1)
# ___________________________________________________________
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
import re
my_list = []
list_num = 0
while list_num < 8:
    b = random.randint(1000, 10000)
    list_num += 1
    my_list.append(b)
print(my_list)
num = input('Введите одну цифру которую нужно удалить из каждого числа: ')
my_list1 = str(my_list)
my_list1 = re.sub(num, "", my_list1)
print(my_list1)

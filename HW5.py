
# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# a = int(input("Введите число: "))
# b = int(input("Введите степень числа(целое неотрицательно число): "))
# def funcExp(a, b):
#     if b == 0:
#         return 1
#     return a * funcExp(a, b - 1)
#
# print(funcExp(a, b))



# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#   4

# a = int(input("Введите первое неотрицительное число "))
# b = int(input("Введите второе неотрицательно число "))
# def recursSum(a, b):
#     if a == 0:
#         return b
#     else:
#         return recursSum(a - 1, b + 1)
#
# print(recursSum(a, b))
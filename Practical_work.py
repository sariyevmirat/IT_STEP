#Задание №1.
# a = int(input("Введите целостное число а "))
# b = int(input("Введите целостное число b "))
# str = a > b
# print (str)

#Задание №2.
# a = int(input("Введите целостное число а "))
# b = int(input("Введите целостное число b "))
# c = int(input("Введите целостное число c "))
# str = a + b > c
# print(str)

#Задание №3.
# a = int(input("Введите целостное число а "))
# str = a % 2 == 0
# print(str)

#Задание №4.
# a = int(input("Введите целостное число а "))
# if a % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

#Задание №5.
# a = int(input("Введите номер дня недели "))
# if a > 0 and a < 6:
#     print("Будний день")
# elif a > 5 and a < 8:
#     print("Выходной день")
# else:
#     print("Ошибка")

#Задание №1.
# n = int(input("Введите целое число n "))
# if n > 20:
#     print(n / 6)
# else:
#     print(n * 6)

#Задание №2.
# n = int(input("Введите целое число n "))
# if n > 0:
#     print (n + 1)
# elif n == 0:
#     print(10)
# else:
#     print(n-2)

#Задание №3.
# a = int(input("Введите целое число a "))
# b = int(input("Введите целое число b "))
# if a != b:
#     print(a + b, b + a)
# else:
#     print(0, 0)

#Задание №4.
# n = int(input("Введите целое число n "))
# if n > 0:
#     print(n + 1)
# else:
#     print(n)

#Задание №5.
# a = int(input("Введите целое число a "))
# b = int(input("Введите целое число b "))
# if a % b == 0:
#     print("Divisible")
# else:
#     print("Not divisible")

#Задание №1.
# A = int(input("Введите цифру "))
# B = int(input("Введите цифру "))
# H = int(input("Введите цифру "))
# if H >= A and H < B:
#     print("Это нормально")
# elif H < A:
#     print("Недосып")
# else:
#     print("Пересып")

#Задание №2.
# y = int(input("Введите год "))
# if  y % 4==0 and y % 100 != 0 or y % 400 == 0:
#     print("Високосный год")
# else:
#     print("Обычный год")

#Задание №3.
# a = int(input("Введите цифру "))
# if a > -15 and a <= 12 or a >= 14 and a < 17 or a >= 19:
#     print("True")
# else:
#     print("False")

#Задание №4.
# f = input("Введите форму фигуры ")
# constant = 3.14
# if f == "Треугольник":
#     a = int(input("Введите а "))
#     b = int(input("Введите b "))
#     c = int(input("Введите c "))
#     print((a+b+c)/2)
# elif f == "Прямоугольник":
#     a = int(input("Введите а "))
#     b = int(input("Введите b "))
#     print(a * b)
# elif f == "Круг":
#     r = int(input("Введите r "))
#     print(constant * r ** 2)
# else:
#     print("Ошибка")

#Задание №5.
# n = int(input("Введите число n "))
# if n == 0 or n >= 5:
#     print(n, "программистов")
# elif n == 1:
#     print(n, "программист")
# elif n >= 2 and n < 5:
#     print(n, "программиста")
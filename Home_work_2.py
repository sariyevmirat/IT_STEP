#Задание №1.
# a = int(input())
# b = int(input())
# str = a
# while str % b != 0:
#     str += a
# print(str)

#Задание №1.
# n = int(input())
# factorial = 1
# sum = 0
# for i in range(1, n + 1):
#     factorial *= i
#     sum += factorial
# print(sum)

#Задание №2.
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, sep='', end='')
#     print()

#Задание №1.
# n = int(input())
# y = 0
# for i in range(1, n + 1):
#     y += i
# for i in range(n - 1):
#     y -= int(input())
# print(y)

#Задание №2.
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1
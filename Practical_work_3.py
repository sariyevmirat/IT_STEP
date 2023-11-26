
#Задание №1.
# x, y = input("Enter two number in one line ").split()
# x = int(x)
# y = int(y)
# def add(x, y):
#     return x + y
# def sub(x, y):
#     return x - y
# print("The sum of numbers is", add(x, y), ", the difference of numbers is", sub(x, y))

#Задание №2. Тоже не мог решить

# Задание №3.
# def power(a, n):
#     result = 1
#     for i in range(n):
#         result *= a
#     return result
# print(power(float(input()), int(input())))

#Задание №4.

#Задание №1.
# a, b = input("Enter numbers: ").split()
# a = int(a)
# b = int(b)
# def pwr(a, b):
#     if b == 0:
#         return 1
#     if b < 0:
#       	return 1 / pwr(a, 0 - b)
#     else:
#         return a * pwr(a,b-1)
# print(f"{a} to the {b} power is", pwr(a, b))

#Задание №2.
# a, b = input("Enter numbers: ").split()
# a = int(a)
# b = int(b)
# def add(a, b):
#     if a == b:
#         return a
#     return a + add(a + 1, b)
# print(f"Sum from {a} to {b} is", add(a, b))

#Задание №3.
# def stars(n):
#     return ' ' if n<=0 else "*"+stars(n-1)
# print(stars(int(input("Enter amount of stars: "))))

#Задание №4.
a = float(input())
n = int(input())
def power(a, n):
    if n == 0:
        return 1
    if n < 0:
      	return 1 / power(a, 0 - n)
    else:
        return a * power(a, n - 1)

print(power(a, n))
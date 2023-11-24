#Задание №1.
# a = 2
# b = 0
# while b <= 20:
#     print(a ** b)
#     b= b + 1

#Задание №2.
# i = 0
# while i < 5:
#     print("*")
#     if i % 2 == 0:
#         print("**")
#     if i > 2:
#         print("***")
#     i = i + 1

#Задание №3.
# a = int(input())
# b = 0
# while a != 0:
#     b = b + a
#     a = int(input())
# print(b)

#Задание №1.
# a = int(input())
# b = int(input())
# for a in range (a, b+1): #1 условие показать все числа в диапазоне
#     print(a)
# for a in range (a, b+1): #2 условие показать нечетные числа в диапазоне
#     if a % 2 != 0:
#         print(a)
# for a in range (a, b+1): #3 условие показать четные числа в диапазоне
#     if a % 2 != 1:
#         print(a)
# for a in range (b, a-1,-1): #4 условие показать в убывающем порядке в диапазоне
#      print(a)

#Задание №2.
# a =int (input())
# b =int (input())
# c =int (input())
# d =int (input())
# for g in range (c,d+1):
#     print('\t'+str(g),end='')
# print(end='\n')
# for i in range (a,b+1):
#     print(str(i)+'\t',end='')
#     for j in range (c,d+1):
#         print(str(i*j),end='\t')
#     print(end='\n')

#Задание №1.
# a="*****"
# x=0
# for i in a:
#     x = x+1
#     print(a[0:x])
#
# for i in a:
#     x = x-1
#     print(a[0:x])

#Задание №2.
# a = 0
# while a<=100:
#   a = int(input())
#   if a<10:
#     continue
#   if a > 100:
#     break
#   print(a)

#Задание №3. Совершенные числа не мог сделать
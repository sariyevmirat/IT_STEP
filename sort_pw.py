#Задание №1.
# def IsAscending(A):
#         i = 1
#         while i <= len(A) - 1 and A[i] > A[i - 1]:
#                 i += 1
#         return 'YES' if i == len(A) else 'NO'
# A = list(map(int,input().split()))
# print(IsAscending(A))

#Задание №2.

#Задание №1.
# s, n = map(int, input().split())
# a = []
# for i in range(n):
#     a.append(int(input()))
# a = sorted(a)
# i = 0
# sum = a[0]
# while sum < s and i < len(a):
#     i += 1
#     if i < len(a):
#         sum += a[i]
# print(i)

#Задание №2.
# tariffs = sorted([int(s) for s in input().split()])
# distances = sorted([int(s) for s in input().split()], reverse=True)
# print(sum(t*d for t, d in zip(tariffs, distances)))
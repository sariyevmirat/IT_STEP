#Задание №1.
print("Fibonacci number ")
def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(int(input())))

#Задание №2.
a = int(input(a))
def sqr(a):
    if a / 2:
        return 1

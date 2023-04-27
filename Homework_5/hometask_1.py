# Задача 26: Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def triangle_number(n):
    if n == 1:
        return 1
    else:
        return n + triangle_number(n-1)
    
n = int(input("Введите число: "))

print("Факториал числа", n, "равен", factorial(n))
print("Треугольное число для", n, "равно", triangle_number(n))
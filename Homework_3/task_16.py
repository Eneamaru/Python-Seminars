# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input("Введите количество элементов в массиве: "))

A = []

for i in range(n):
    A.append(int(input("Введите число: ")))

x = int(input("Введите число, которое нужно найти: "))

count = 0
for i in range(n):
    if A[i] == x:
        count += 1

print("Число", x, "встречается в массиве", count, "раз(а).")
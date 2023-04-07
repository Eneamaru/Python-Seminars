# Задача 2: Найдите сумму цифр трехзначного числа.

number = 123

a = number // 100
b = number % 100 // 10
c = number % 10

sum = a + b + c

print(sum)
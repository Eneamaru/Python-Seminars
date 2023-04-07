# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите количество долек по вертикали: "))
m = int(input("Введите количество долек по горизонтали: "))
k = int(input("Сколько долек вы хотите отломить?: "))

sum = n * m

if k <= sum and (k % n == 0 or k % m == 0):
    print("Да, вы можете столько отломить")
else:
    print("К сожалению столько отломить не получится")
# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

min_val = int(input("Введите нижнее значение диапазона: "))
max_val = int(input("Введите верхнее значение диапазона: "))

my_list = [1, -5, -3, 8, 6, -4, 7]

result = []
for i in range(len(my_list)):
    if my_list[i] >= min_val and my_list[i] <= max_val:
        result.append(i)

print("Индексы элементов списка, которые попадают в диапазон от", min_val, "до", max_val, ":")
print(result)
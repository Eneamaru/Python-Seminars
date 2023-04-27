# Заданный диапазон
min_val = int(input("Введите нижнее значение диапазона: "))
max_val = int(input("Введите верхнее значение диапазона: "))

# Исходный список
my_list = [1, -5, -3, 8, 6, -4, 7]

# Создаем список индексов элементов, которые попадают в заданный диапазон
result = []
for i in range(len(my_list)):
    if my_list[i] >= min_val and my_list[i] <= max_val:
        result.append(i)

print("Индексы элементов списка, которые попадают в диапазон от", min_val, "до", max_val, ":")
print(result)
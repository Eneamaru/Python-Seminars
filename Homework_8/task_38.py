import os

def read_phonebook():
    if not os.path.exists("phonebook.txt"):
        return []
    with open("phonebook.txt", "r") as f:
        lines = f.readlines()
    phonebook = []
    for line in lines:
        surname, name, patronymic, phone = line.strip().split(",")
        phonebook.append((surname, name, patronymic, phone))
    return phonebook

def write_phonebook(phonebook):
    with open("phonebook.txt", "w") as f:
        for record in phonebook:
            f.write(",".join(record) + "\n")

def add_record():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите телефонный номер: ")
    phonebook = read_phonebook()
    phonebook.append((surname, name, patronymic, phone))
    write_phonebook(phonebook)

def display_phonebook():
    phonebook = read_phonebook()
    if not phonebook:
        print("Справочник пуст.")
        return
    for record in phonebook:
        print(f"{record[0]} {record[1]} {record[2]}: {record[3]}")

def search_phonebook():
    search_term = input("Найти запись: ")
    phonebook = read_phonebook()
    results = []
    for record in phonebook:
        if search_term in record:
            results.append(record)
    if not results:
        print("Ничего не найдено.")
        return
    for record in results:
        print(f"{record[0]} {record[1]} {record[2]}: {record[3]}")
    return results

def modify_phonebook():
    surname = input("Введите фамилию: ")
    phonebook = read_phonebook()
    results = []
    for i, record in enumerate(phonebook):
        if surname == record[0]:
            results.append((i, record))
    if not results:
        print("Ничего не найдено")
        return
    for i, record in results:
        print(f"{i}. {record[0]} {record[1]} {record[2]}: {record[3]}")
    choice = input("Выберите запись: ")
    if not choice.isdigit() or int(choice) >= len(results):
        print("Неверный выбор.")
        return
    i, record = results[int(choice)]
    surname = input(f"Введите новую фамилию ({record[0]}): ") or record[0]
    name = input(f"Введите новое имя ({record[1]}): ") or record[1]
    patronymic = input(f"Введите новое отчество ({record[2]}): ") or record[2]
    phone = input(f"Введите новый телефонный номер ({record[3]}): ") or record[3]
    phonebook[i] = (surname, name, patronymic, phone)
    write_phonebook(phonebook)

def delete_phonebook():
    surname = input("Введите фамилию: ")
    phonebook = read_phonebook()
    results = []
    for i, record in enumerate(phonebook):
        if surname == record[0]:
            results.append((i, record))
    if not results:
        print("Ничего не найдено.")
        return
    for i, record in results:
        print(f"{i}. {record[0]} {record[1]} {record[2]}: {record[3]}")
    choice = input("Выберите запись: ")
    if not choice.isdigit() or int(choice) >= len(results):
        print("Неверный выбор.")
        return
    i, record = results[int(choice)]
    phonebook.pop(i)
    write_phonebook(phonebook)

def main():
    while True:
        print("1. Добавить запись")
        print("2. Показать записи")
        print("3. Найти запись")
        print("4. Изменить запись")
        print("5. Удалить запись")
        print("6. Выход")
        choice = input("Выберите пункт: ")
        if choice == "1":
            add_record()
        elif choice == "2":
            display_phonebook()
        elif choice == "3":
            search_phonebook()
        elif choice == "4":
            modify_phonebook()
        elif choice == "5":
            delete_phonebook()
        elif choice == "6":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()

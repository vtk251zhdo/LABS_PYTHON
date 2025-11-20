import os
from datetime import datetime
import time
import re

def Task1():
    
    if not os.path.exists("numbers.txt"):
        print("Помилка: файл numbers.txt не знайдено!")
        return

    numbers = []

    with open("numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            value = line.strip()
            if value.lstrip("-").replace(".", "", 1).isdigit():
                numbers.append(float(value))
            else:
                print("Помилка: знайдено не число у файлі -", value)
                return

    if len(numbers) == 0:
        print("Помилка: файл порожній або не містить чисел!")
        return

    total = sum(numbers)

    print("Сума чисел з файла:", total)

    with open("sum_numbers.txt", "w", encoding="utf-8") as f:
        f.write(str(total))


def Task2():
    
    nums = input("Введіть довільну кількість цілих чисел через пробіл: ").split()

    if len(nums) == 0:
        print("Помилка: не введено чисел!")
        return

    results = []

    for value in nums:
        if value.lstrip("-").isdigit():
            n = int(value)
            if n % 2 == 0:
                results.append(f"{n} — парне")
            else:
                results.append(f"{n} — непарне")
        else:
            print("Помилка: некоректне число - ", value)
            return

    with open("parity.txt", "w", encoding="utf-8") as f:
        for line in results:
            f.write(line + "\n")

    print("Результат записано у parity.txt")

def Task3():
    
    filename = "learning_python.txt"

    if not os.path.exists(filename):
        print("Помилка: файл learning_python.txt не знайдено!")
        return

    lines = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            text = line.strip()
            if text:
                lines.append(text)

    if len(lines) == 0:
        print("Помилка: файл порожній!")
        return

    print("Текст з файла:")
    for l in lines:
        print(l)

    sorted_lines = sorted(lines, key=len, reverse=True)

    print("\nРядки від найдовшого до найкоротшого: ")
    for l in sorted_lines:
        print(l)
        
def Task4():
    source = "learning_python.txt"

    if not os.path.exists(source):
        print("Помилка: файл learning_python.txt не знайдено!")
        return

    with open(source, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]

    if len(lines) == 0:
        print("Помилка: файл порожній!")
        return

    folder = "Task4_output"
    if not os.path.exists(folder):
        os.mkdir(folder)

    changed_file = os.path.join(folder, "learning_c.txt")
    true_file = os.path.join(folder, "true_statements.txt")
    false_file = os.path.join(folder, "false_statements.txt")

    changed_lines = [l.replace("Python", "C") for l in lines]

    with open(changed_file, "w", encoding="utf-8") as f:
        for l in changed_lines:
            f.write(l + "\n")

    print("\nЗмінені фрази:\n")

    true_list = []
    false_list = []

    for l in changed_lines:
        print(l)
        ans = input("Чи є фраза істинною для мови C? (так/ні): ").strip().lower()

        if ans == "так":
            true_list.append(l)
        elif ans == "ні":
            false_list.append(l)
        elif ans == "yes":
            false_list.append(l)
        elif ans == "no":
            false_list.append(l)
        else:
            print("Некоректна відповідь, пропуск")
            false_list.append(l)

    with open(true_file, "w", encoding="utf-8") as f:
        for l in true_list:
            f.write(l + "\n")

    with open(false_file, "w", encoding="utf-8") as f:
        for l in false_list:
            f.write(l + "\n")

    print("\nОпрацювання завершено!")
    print("Істинні твердження записано у: ", true_file)
    print("Хибні твердження записано у: ", false_file)

def Task5():
    
    filename = "guest_book.txt"

    if not os.path.exists(filename):
        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Файл створено: " + created + "\n")
            f.write("Остання зміна: " + created + "\n\n")

    while True:
        name = input("Введіть ім'я (або 'вихід'): ").strip()

        if name.lower() == "вихід":
            print("Вихід у головне меню.")
            return

        if name == "":
            print("Помилка: ім’я порожнє!")
            continue

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        greeting = f"Вітаю, {name}! — {timestamp}"
        print(greeting)

        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        lines[1] = "Остання зміна: " + timestamp + "\n"

        with open(filename, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line)
            f.write(greeting + "\n")

def main():
    
    while True:
        print("\nЗавдання:")
        print("1 — Завдання 1 (сума з файла)")
        print("2 — Завдання 2 (парність чисел)")
        print("3 — Завдання 3 (довжина рядків)")
        print("4 — Завдання 4 (перекладач)")
        print("5 — Завдання 5 (Вітальник)")
        print("0 — Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            Task1()
        elif choice == "2":
            Task2()
        elif choice == "3":
            Task3()
        elif choice == "4":
            Task4()
        elif choice == "5":
            Task5()
        elif choice == "6":
            Task6()
        elif choice == "0":
            print("Вихід!")
            break
        else:
            print("Помилка вибору!")


main()

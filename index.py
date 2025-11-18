import random

def Task1():

    num = input("Введіть кількість елементів списку: ")

    if not num.isdigit():
        print("Помилка: потрібно ввести додатне число!")
        exit()

    num = int(num)

    if num <= 0:
        print("Помилка: кількість елементів має бути більшою за 0!")
        exit()

    numbers = []
    for i in range(num):
        value = input(f"Введіть елемент №{i + 1}: ")

        if value.lstrip("-").isdigit():
            numbers.append(int(value))
        else:
            print("Помилка: введено не ціле число!")
            exit()

    max_value = max(numbers)

    print("Максимальний елемент списку: ", max_value)
    print("Список у зворотному порядку: ", numbers[::-1])

def Task2():

    n = input("Введіть кількість елементів списку: ")

    if not n.isdigit():
        print("Помилка: потрібно ввести додатне число!")
        exit()

    n = int(n)

    if n <= 0:
        print("Помилка: кількість елементів повинна бути більшою за 0!")
        exit()

    numbers = []
    for i in range(n):
        value = input(f"Введіть елемент №{i + 1}: ")

        if value.lstrip("-").isdigit():
            numbers.append(int(value))
        else:
            print("Помилка: введено не ціле число!")
            exit()

    positive = []
    others = []

    for num in numbers:
        if num > 0:
            positive.append(num)
        else:
            others.append(num)

    print("Початковий список: ", numbers)
    print("Додатні елементи: ", positive)
    print("Інші елементи (нуль і від’ємні): ", others)

def Task3():

    print("Оберіть спосіб заповнення списку: ")
    print("1 — Ввести 20 чисел вручну")
    print("2 — Згенерувати 20 випадкових чисел")

    choice = input("Ваш вибір (1 або 2): ")

    if choice not in ("1", "2"):
        print("Помилка: потрібно вибрати 1 або 2!")
        exit()

    numbers = []

    if choice == "1":
        print("Введіть 20 цілих чисел: ")
        for i in range(20):
            value = input(f"Елемент №{i + 1}: ")

            if value.lstrip("-").isdigit():
                numbers.append(int(value))
            else:
                print("Помилка: потрібно вводити лише цілі числа!")
                exit()

    else:
        numbers = [random.randint(-100, 100) for _ in range(20)]
        print("Список автоматично згенеровано.")

    total = 0
    for i in range(1, 20, 2): 
        total += numbers[i]

    print("Початковий список: ", numbers)
    print("Сума елементів: ", total)

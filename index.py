
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
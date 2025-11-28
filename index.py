import random

# Завдання 1

class Bank:
    def __init__(self, balance):
        if not isinstance(balance, (int, float)):
            raise TypeError("Початковий баланс має бути числом")
        if balance < 0:
            raise ValueError("Початковий баланс не може бути від’ємним")
        self.__balance = float(balance)

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Сума має бути числом")
        if amount <= 0:
            raise ValueError("Сума поповнення повинна бути більшою за нуль")
        self.__balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Сума має бути числом")
        if amount <= 0:
            raise ValueError("Сума зняття повинна бути більшою за нуль")
        if amount > self.__balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self.__balance -= amount

    def get_balance(self):
        return round(self.__balance, 2)

def Task1():
    try:
        start = float(input("Введіть початковий баланс: "))
        acc = Bank(start)

        while True:
            print("\nОперації:")
            print("1 — Поповнити рахунок")
            print("2 — Зняти кошти")
            print("3 — Показати баланс")
            print("0 — Повернутись у головне меню")

            op = input("Ваш вибір: ")

            if op == "1":
                amount = float(input("Сума поповнення: "))
                acc.deposit(amount)
                print("Операція виконана")
            elif op == "2":
                amount = float(input("Сума зняття: "))
                acc.withdraw(amount)
                print("Операція виконана")
            elif op == "3":
                print("Поточний баланс:", acc.get_balance())
            elif op == "0":
                break
            else:
                print("Помилка вибору!")

    except Exception as e:
        print("Помилка:", e)

# Завдання 1



def main():
    while True:
        print("\nЗавдання:")
        print("1 — Завдання 1")
        print("2 — Завдання 2")
        print("3 — Завдання 3")
        print("0 — Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            Task1()
        elif choice == "2":
            Task2()
        elif choice == "0":
            print("Вихід!")
            break
        else:
            print("Помилка вибору!")


main()

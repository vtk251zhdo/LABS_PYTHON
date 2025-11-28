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

# Завдання 2

class Coin:
    def __init__(self):
        self.__sideup = random.choice(["heads", "tails"])

    def toss(self):
        self.__sideup = random.choice(["heads", "tails"])
        return self.__sideup
    
def Task2():
    try:
        n = int(input("Скільки разів підкидати монету: "))
        if n <= 0:
            print("Кількість повинна бути більшою за нуль")
            return

        coin = Coin()

        for i in range(n):
            print(f"Підкидання {i+1}: {coin.toss()}")

    except Exception as e:
        print("Помилка:", e)

# Завдання 2

# Завдання 3

class Car:
    def __init__(self, make, model, year):
        if not isinstance(make, str) or not isinstance(model, str):
            raise TypeError("Марка і модель мають бути текстом")
        if not isinstance(year, int) or year <= 1800:
            raise ValueError("Невірний рік виробництва")

        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed = max(0, self.speed - 5)

    def get_speed(self):
        return self.speed
      
def Task3():
    try:
        make = input("Марка: ")
        model = input("Модель: ")
        year = int(input("Рік випуску: "))

        car = Car(make, model, year)

        print("\nПрискорення:")
        for _ in range(5):
            car.accelerate()
            print("Швидкість:", car.get_speed())

        print("\nГальмування:")
        for _ in range(5):
            car.brake()
            print("Швидкість:", car.get_speed())

    except Exception as e:
        print("Помилка:", e)

# Завдання 3

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
        elif choice == "3":
            Task2()
        elif choice == "0":
            print("Вихід!")
            break
        else:
            print("Помилка вибору!")


main()

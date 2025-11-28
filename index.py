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

# Завдання 4

class Dog:
    mammal = "ссавець"
    nature = "невідомий"
    breed = "невідома порода"

    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError("Ім'я має бути текстом")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Вік має бути додатним числом")

        self.name = name
        self.age = age

    def info(self):
        return f"{self.name}, {self.age} років, {self.breed}, характер: {self.nature}"

    def voice(self):
        return f"{self.name} каже: гав"


class Husky(Dog):
    nature = "активний, енергійний"
    breed = "husky"

    def run(self):
        return f"{self.name} біжить як вітер"


class Bulldog(Dog):
    nature = "спокійний, ледачкуватий"
    breed = "bulldog"

    def guard(self):
        return f"{self.name} охороняє територію"


class Chihuahua(Dog):
    nature = "емоційний, голосний"
    breed = "chihuahua"

    def squeak(self):
        return f"{self.name} подає високий голос"


class Pets:
    def __init__(self, pets_list):
        self.pets_list = pets_list

    def show_all(self):
        for pet in self.pets_list:
            print(pet.info())
            print("Поводження:", self.get_behavior(pet))
            print()

    def get_behavior(self, pet):
        if isinstance(pet, Husky):
            return pet.run()
        if isinstance(pet, Bulldog):
            return pet.guard()
        if isinstance(pet, Chihuahua):
            return pet.squeak()
        return pet.voice()

def Task4():
    try:
        dog1 = Husky("Рекс", 3)
        dog2 = Bulldog("Бім", 5)
        dog3 = Chihuahua("Тіна", 2)

        my_pets = Pets([dog1, dog2, dog3])

        print("\nВаші домашні улюбленці:\n")
        my_pets.show_all()

    except Exception as e:
        print("Помилка:", e)

# Завдання 4

# Завдання 5

class Buffer:
    def __init__(self):
        self.data = []

    def add(self, *a):
        for x in a:
            if not isinstance(x, int):
                raise TypeError("Усі елементи мають бути цілими числами")
            self.data.append(x)

            if len(self.data) == 5:
                print(sum(self.data))
                self.data = []

    def get_current_part(self):
        return self.data[:]

def Task5():
    try:
        buf = Buffer()

        buf.add(1, 2, 3)
        print("Поточні дані:", buf.get_current_part())

        buf.add(4, 5, 6)
        print("Поточні дані:", buf.get_current_part())

        buf.add(7, 8)
        print("Поточні дані:", buf.get_current_part())

        buf.add(9, 10, 11, 12, 13, 14)
        print("Поточні дані:", buf.get_current_part())

    except Exception as e:
        print("Помилка:", e)

# Завдання 5

# Завдання 6

class NameTooShortError(ValueError):
    pass

def check_name(name):
    if not isinstance(name, str):
        raise TypeError("Ім'я має бути текстом")
    if len(name) < 10:
        raise NameTooShortError("Ім'я занадто коротке")

def Task6():
    try:
        name = input("Введіть ім'я: ")
        check_name(name)
        print("Ім'я прийнято")
    except Exception as e:
        print("Помилка:", e)

# Завдання 6

# Завдання 7

class DecimalRoman:
    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError("Число має бути= цілим")
        if number <= 0 or number >= 3999:
            raise ValueError("Число має бути в діапазоні від 1 до 3999")
        self.number = number

    def convert(self):
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (300, "CCC"), (200, "CC"), (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"), (30, "XXX"), (20, "XX"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        result = ""
        num = self.number
        for value, symbol in roman_map:
            while num >= value:
                result += symbol
                num -= value
        return result
    
class RomanDecimal:
    def __init__(self, roman):
        if not isinstance(roman, str):
            raise TypeError("Римське число має бути текстом")
        self.roman = roman.upper()

    def convert(self):
        roman_values = {
            "M": 1000, "D": 500, "C": 100,
            "L": 50, "X": 10, "V": 5, "I": 1
        }
        total = 0
        prev = 0

        for char in reversed(self.roman):
            if char not in roman_values:
                raise ValueError("Некоректний римський символ")
            value = roman_values[char]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value

        return total
    
def Task7():
    try:
        print("\n1 — Десяткове в Римське")
        print("2 — Римське в Десяткове")
        choice = input("Ваш вибір: ")

        if choice == "1":
            num = int(input("Введіть десяткове число: "))
            conv = DecimalRoman(num)
            print("Результат:", conv.convert())

        elif choice == "2":
            r = input("Введіть римське число: ")
            conv = RomanDecimal(r)
            print("Результат:", conv.convert())

        else:
            print("Помилка вибору.")
    except Exception as e:
        print("Помилка:", e)
    
# Завдання 7

def main():
    while True:
        print("\nЗавдання:")
        print("1 — Завдання 1")
        print("2 — Завдання 2")
        print("3 — Завдання 3")
        print("4 — Завдання 4")
        print("5 — Завдання 5")
        print("6 — Завдання 6")
        print("7 — Завдання 7")
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
        elif choice == "7":
            Task7()
        elif choice == "0":
            print("Вихід!")
            break
        else:
            print("Помилка вибору!")

main()

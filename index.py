# Task 1 - Alpahabet


def Task1():

    class Alphabet:

        ua_lang = "UA"
        ua_letters = list("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")

        def __init__(self, lang=ua_lang, letters=ua_letters):
            if not isinstance(letters, (list, str)):
                raise TypeError("Letters must be list or string")

            self.lang = lang
            self.letters = list(letters)

        def print_alphabet(self):
            print(" ".join(self.letters))

        def letters_num(self):
            return len(self.letters)

        def is_ua_lang(self, text):
            if not isinstance(text, str):
                return False
            text = text.lower()
            return all(char in self.ua_letters or not char.isalpha() for char in text)

    class EngAlphabet(Alphabet):
        __en_letters_num = 26

        def __init__(self):
            super().__init__("EN", "abcdefghijklmnopqrstuvwxyz")

        def is_en_letter(self, letter):
            if not isinstance(letter, str) or len(letter) != 1:
                return False
            return letter.lower() in self.letters

        def letters_num(self):
            return self.__en_letters_num

        @staticmethod
        def example():
            return "Jack was hungry. He walked to the kitchen. He got out some eggs. He took out some oil. He placed a skillet on the stove. Next, he turned on the heat. He poured the oil into the skillet. He cracked the eggs into a bowl. He stirred the eggs. Then, he poured them into the hot skillet. He waited while the eggs cooked. They cooked for two minutes. He heard them cooking. They popped in the oil."

    #  --- TESTS ---
    print("\n--- RESULT ---")
    eng = EngAlphabet()
    eng.print_alphabet()
    print("Letters count:", eng.letters_num())
    print("Is 'J' English?", eng.is_en_letter("J"))

    ua = Alphabet()
    print("Is 'Щ' Ukrainian?", ua.is_ua_lang("Щ"))
    print("Example:", EngAlphabet.example())


# Task 2 - HUMAN / HOUSE


def Task2():

    class House:

        def __init__(self, area=100, price=100000):

            if area <= 0 or price <= 0:
                raise ValueError("Area and price must be positive")
            self._area = area
            self._price = price

        def final_price(self, discount):
            if not 0 <= discount <= 100:
                raise ValueError("Invalid discount")
            return self._price * (1 - discount / 100)

    class SmallHouse(House):
        def __init__(self, price=50000):
            super().__init__(40, price)

    class Human:
        default_name = "Zhukovskyi Danyil"
        default_age = 19

        def __init__(self, name, age, money=0, house=None):
            if age <= 0:
                raise ValueError("Age must be positive")

            self.name = name
            self.age = age
            self.__money = money
            self.__house = house

        def info(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Money: {self.__money}")
            print(f"House: {self.__house}")

        @staticmethod
        def default_info():
            print(f"Default name: {Human.default_name}")
            print(f"Default age: {Human.default_age}")

        def earn_money(self, amount):
            if amount <= 0:
                print("Invalid income amount")
                return
            self.__money += amount

        def __make_deal(self, house, price):
            self.__money -= price
            self.__house = house

        def buy_house(self, house, discount=10):
            if not isinstance(house, House):
                print("Invalid house object")
                return

            final_price = house.final_price(discount)

            if self.__money >= final_price:
                self.__make_deal(house, final_price)
                print("House purchased successfully!")
            else:
                print("Not enough money to buy the house.")

    #  --- TESTS ---
    print("\n--- RESULT ---")
    Human.default_info()

    person = Human("Eloquencert", 21, 10000)
    person.info()

    small_house = SmallHouse()
    person.buy_house(small_house)

    person.earn_money(50000)
    person.buy_house(small_house)
    person.info()


# Task 3 - APPLE


def Task3():

    class Apple:

        states = ["Absent", "Flowering", "Green", "Red"]

        def __init__(self, index):
            self._index = index
            self._state = Apple.states[0]

        def grow(self):
            curerent = Apple.states.index(self._state)
            if curerent < len(Apple.states) - 1:
                self._state = Apple.states[curerent + 1]
        
        def is_ripe(self):
            return self._state == Apple.states[-1]


    class AppleTree:
        def __init__(self, count):
            if count <= 0:
                raise ValueError("Apple count must be positive")
            self.apples = [Apple(i + 1) for i in range(count)]

        def grow_all(self):
            for apple in self.apples:
                apple.grow()

        def all_are_ripe(self):
            return all(apple.is_ripe() for apple in self.apples)

        def give_away_all(self):
            self.apples.clear()

    class Gardener:
        def __init__(self, name, tree):
            self.name = name
            self._tree = tree

        def work(self):
            self._tree.grow_all()

        def harvest(self):
            if self._tree.all_are_ripe():
                self._tree.give_away_all()
                print("Harvested all apples!")
            else:
                print("Apples are not ripe yet")

        @staticmethod
        def apple_base(apples):
            for apple in apples:
                print(f"Apple #{apple._index}: {apple._state}")
            
# ===== TESTS PART 3 =====
    print("\n--- RESULT ---")
    tree = AppleTree(3)
    gardener = Gardener("Ivan", tree)

    Gardener.apple_base(tree.apples)

    while not tree.all_are_ripe():
        gardener.work()
        Gardener.apple_base(tree.apples)

    gardener.harvest()                 


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
            Task3()

        elif choice == "0":
            print("Вихід!")
            break
        else:
            print("Помилка вибору!")


main()

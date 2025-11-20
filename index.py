from datetime import date

def Task1():

    class Person:

        def __init__(self, surname, first_name, birth_date_str, nickname=None):

            self.surname = surname
            self.first_name = first_name
            self.nickname = nickname

            year, month, day = birth_date_str.split("-")
            year = int(year)
            month = int(month)
            day = int(day)

            self.birth_date = date(year, month, day)

        def get_age(self):
            today = date.today()
            age = today.year - self.birth_date.year

            if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
                age -= 1

            return str(age)

        def get_fullname(self):
            return f"{self.surname} {self.first_name}"
        
    p_1 = Person("Жуковський", "Даниіл", "2006-06-28", "Eloquencert")

    print(p_1.get_fullname()) 
    print(p_1.get_age())      
    print(p_1.nickname)

def Task2():

    class Person:
        def __init__(self, surname, first_name, birth_date_str, nickname=None):
            year, month, day = birth_date_str.split("-")
            self.surname = surname
            self.first_name = first_name
            self.nickname = nickname
            self.birth_date = date(int(year), int(month), int(day))

        def get_fullname(self):
            return f"{self.surname} {self.first_name}"

        def get_age(self):
            today = date.today()
            age = today.year - self.birth_date.year
            if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
                age -= 1
            return str(age)
    
    filename = "InfoPeople.txt"
    people = []

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header = lines[0].strip().split(",")

    data_lines = lines[1:]

    for line in data_lines:
        parts = line.strip().split(",")

        surname = parts[0].strip()
        first_name = parts[1].strip()
        nickname = parts[2].strip() if parts[2].strip() != "" else None
        birth_date = parts[3].strip()

        person = Person(surname, first_name, birth_date, nickname)
        people.append(person)

    new_header = ["surname", "name", "fullname", "nickname", "birth_date", "age"]

    with open(filename, "w", encoding="utf-8") as f:
        f.write(",".join(new_header) + "\n")

        for p in people:
            row = [
                p.surname,
                p.first_name,
                p.get_fullname(),
                p.nickname if p.nickname else "",
                p.birth_date.isoformat(),
                p.get_age()
            ]
            f.write(",".join(row) + "\n")

    print("Файл оновлено!")

def main():
    
    while True:
        print("\nЗавдання:")
        print("1 — Завдання 1")
        print("2 — Завдання 2")
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
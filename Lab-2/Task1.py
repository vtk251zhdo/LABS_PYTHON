import random

def task1():
    random_integers = [random.randint(0, 100) for _ in range(20)]
    selected_integers = [num for num in random_integers if num <= 50]
    print("Випадкові числа:", random_integers)
    print("Числа з першої половини інтервалу (0–50):", selected_integers)


def task2():
    purchase_amount = float(input("Введіть суму покупки: "))
    discount = 0
    if purchase_amount > 1000:
        discount = 0.05
    elif purchase_amount > 500:
        discount = 0.03
    discounted_price = purchase_amount * (1 - discount)
    print(f"Початкова сума: {purchase_amount} грн")
    print(f"Знижка: {discount * 100}%")
    print(f"Сума до сплати: {discounted_price:.2f} грн")


def task3():
    base = float(input("Введіть основу рівнобедреного трикутника: "))
    height = float(input("Введіть висоту рівнобедреного трикутника: "))
    area = (base * height) / 2
    if area % 2 == 0:
        print(f"Площа трикутника парна. Поділена на 2: {area / 2}")
    else:
        print("Не можу ділити на 2!")


def task4():
    A = int(input("Введіть число A (A < B): "))
    B = int(input("Введіть число B (A < B): "))
    if A >= B:
        print("Помилка: A має бути менше за B.")
    else:
        total_sum = sum(range(A, B + 1))
        print(f"Сума всіх цілих чисел від {A} до {B}: {total_sum}")


def task5():
    A = int(input("Введіть число A: "))
    B = int(input("Введіть число B: "))
    if A >= B:
        print("Помилка: A має бути менше за B")
    else:
        sum_of_squares = sum(i ** 2 for i in range(A, B + 1))
        print(f"Сума квадратів чисел від {A} до {B}: {sum_of_squares}")


def task6():
    a = int(input("Введіть значення a: "))
    b = int(input("Введіть значення b: "))
    if b < a:
        print("Помилка: b має бути не менше за a")
    else:
        total_sum = 0
        current = a
        while current <= b:
            total_sum += current
            current += 1
        print(f"Сума чисел від {a} до {b}: {total_sum}")


def task7():
    a = int(input("Введіть число a (0 ≤ a ≤ 50): "))
    if a < 0 or a > 50:
        print("Помилка: значення має бути в межах (0 ≤ a ≤ 50)")
    else:
        sum_of_squares = sum(i ** 2 for i in range(a, 51))
        print(f"Сума квадратів чисел від {a} до 50: {sum_of_squares}")


def task8():
    N = int(input("Введіть число N (N > 1): "))
    if N <= 1:
        print("Помилка: N має бути більше 1")
    else:
        K = 0
        power = 1
        while power <= N:
            K += 1
            power *= 5
        print(f"Найменше ціле K, для якого 5^{K} > {N}: {K}")


def task9():
    n = int(input("Введіть число n: "))
    for i in range(1, n + 2):
        square = i ** 2
        if square > n:
            print(f"Перше число, більше за {n}, серед квадратів: {square}")
            break


def task10():
    n = int(input("Введіть число n: "))
    current = 1
    increment = 1
    while current <= n:
        increment += 2
        current += increment
    print(f"Перше число в послідовності, більше за {n}: {current}")


def task11():
    def get_zodiac_sign(day, month):
        if (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "Водолій"
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            return "Риби"
        elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "Овен"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "Телець"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
            return "Близнюки"
        elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
            return "Рак"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "Лев"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "Діва"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "Терези"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
            return "Скорпіон"
        elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
            return "Стрілець"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "Козоріг"
        else:
            return "Некоректна дата"

    day = int(input("Введіть день: "))
    month = int(input("Введіть місяць: "))
    zodiac_sign = get_zodiac_sign(day, month)
    print(f"Знак зодіаку для дати {day}.{month}: {zodiac_sign}")


def task12():
    unit = int(input("Введіть номер одиниці маси (1: кг, 2: мг, 3: г, 4: т, 5: ц): "))
    mass = float(input("Введіть масу тіла в цих одиницях: "))
    if unit == 1:
        mass_in_kg = mass
    elif unit == 2:
        mass_in_kg = mass / 1_000_000
    elif unit == 3:
        mass_in_kg = mass / 1_000
    elif unit == 4:
        mass_in_kg = mass * 1_000
    elif unit == 5:
        mass_in_kg = mass * 100
    else:
        mass_in_kg = None
        print("Помилка: введіть число від 1 до 5")

    if mass_in_kg is not None:
        print(f"Маса тіла у кілограмах: {mass_in_kg} кг")
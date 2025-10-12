import random

random_integers = [random.randint(0, 100) for _ in range(20)]

selected_integers = [num for num in random_integers if num <= 50]

print("Random integers:", random_integers)
print("Selected integers (0-50):", selected_integers)

purchase_amount = float(input("Enter the purchase amount (UAH): "))

discount = 0
if purchase_amount > 1000:
    discount = 0.05
elif purchase_amount > 500:
    discount = 0.03

discounted_price = purchase_amount * (1 - discount)

print(f"Original amount: {purchase_amount} UAH")
print(f"Discount applied: {discount * 100}%")
print(f"Final amount: {discounted_price:.2f} UAH")

base = float(input("Enter the base of the isosceles triangle: "))
height = float(input("Enter the height of the isosceles triangle: "))

area = (base * height) / 2

if area % 2 == 0:
    print(f"The area of the triangle is even. Divided by 2: {area / 2}")
else:
    print("Cannot divide by 2!")

A = int(input("Enter the value of A (A < B): "))
B = int(input("Enter the value of B (A < B): "))

if A >= B:
    print("Invalid input. Ensure that A < B.")
else:
    total_sum = sum(range(A, B + 1))
    print(f"The sum of integers from {A} to {B} is: {total_sum}")

A = int(input("Enter the value of A (A < B): "))
B = int(input("Enter the value of B (A < B): "))

if A >= B:
    print("Invalid input. Ensure that A < B.")
else:
    sum_of_squares = sum(i**2 for i in range(A, B + 1))
    print(f"The sum of the squares of integers from {A} to {B} is: {sum_of_squares}")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b (b >= a): "))

if b < a:
    print("Invalid input. Ensure that b >= a.")
else:
    total_sum = 0
    current = a
    while current <= b:
        total_sum += current
        current += 1
    print(f"The sum of integers from {a} to {b} is: {total_sum}")

a = int(input("Enter the value of a (0 ≤ a ≤ 50): "))

if a < 0 or a > 50:
    print("Invalid input. Ensure that 0 ≤ a ≤ 50.")
else:
    sum_of_squares = sum(i**2 for i in range(a, 51))
    print(f"The sum of the squares of integers from {a} to 50 is: {sum_of_squares}")

N = int(input("Enter the value of N (N > 1): "))

if N <= 1:
    print("Invalid input. Ensure that N > 1.")
else:
    K = 0
    power = 1  # 5^0 = 1
    while power <= N:
        K += 1
        power *= 5
    print(f"The smallest integer K such that 5^K > {N} is: {K}")

n = int(input("Enter the value of n: "))

for i in range(1, n + 2):  
    square = i ** 2
    if square > n:
        print(f"The first square greater than {n} is: {square}")
        break

n = int(input("Enter the value of n: "))

current = 1
increment = 1

while current <= n:
    increment += 2
    current += increment

print(f"The first number in the sequence greater than {n} is: {current}")

def get_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "Gemini"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
        return "Scorpio"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    else:
        return "Invalid date"

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))

zodiac_sign = get_zodiac_sign(day, month)
print(f"The zodiac sign for {day}/{month} is: {zodiac_sign}")

unit = int(input("Enter the mass unit (1: kilogram, 2: milligram, 3: gram, 4: ton, 5: centner): "))
mass = float(input("Enter the mass of the body in the given unit: "))

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
    print("Invalid unit number. Please enter a number between 1 and 5.")

if mass_in_kg is not None:
    print(f"The mass of the body in kilograms is: {mass_in_kg} kg")
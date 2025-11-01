a = int(input("Введіть число a (0 ≤ a ≤ 50): "))

if a < 0 or a > 50:
    print("Помилка: значення має бути в межах (0 ≤ a ≤ 50)")
else:
    sum_of_squares = sum(i ** 2 for i in range(a, 51))
    print(f"Сума квадратів чисел від {a} до 50: {sum_of_squares}")

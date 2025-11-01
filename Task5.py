A = int(input("Введіть число A: "))
B = int(input("Введіть число B: "))

if A >= B:
    print("Помилка: A має бути менше за B")
else:
    sum_of_squares = sum(i ** 2 for i in range(A, B + 1))
    print(f"Сума квадратів чисел від {A} до {B}: {sum_of_squares}")

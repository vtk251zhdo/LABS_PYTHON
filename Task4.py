A = int(input("Введіть число A (A < B): "))
B = int(input("Введіть число B (A < B): "))

if A >= B:
    print("Помилка: A має бути менше за B.")
else:
    total_sum = sum(range(A, B + 1))
    print(f"Сума всіх цілих чисел від {A} до {B}: {total_sum}")
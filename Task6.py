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

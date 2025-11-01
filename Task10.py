n = int(input("Введіть число n: "))

current = 1
increment = 1

while current <= n:
    increment += 2
    current += increment

print(f"Перше число в послідовності, більше за {n}: {current}")

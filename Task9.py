n = int(input("Введіть число n: "))

for i in range(1, n + 2):
    square = i ** 2
    if square > n:
        print(f"Перше число, більше за {n}, серед квадратів: {square}")
        break

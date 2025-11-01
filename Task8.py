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

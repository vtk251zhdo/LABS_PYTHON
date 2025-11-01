import random

random_integers = [random.randint(0, 100) for _ in range(20)]
selected_integers = [num for num in random_integers if num <= 50]

print("Випадкові числа:", random_integers)
print("Числа з першої половини інтервалу (0–50):", selected_integers)
text = input("Введіть текст українською (до 1000 слів): ")

words = text.replace(",", "").replace(".", "").split()
half = len(words) // 2

first_part = []
second_part = []

for i in range(len(words)):
    if i < half:
        first_part.append(words[i].capitalize())
    else:
        second_part.append(words[i].lower() + "*")

result = " ".join(first_part) + " | " + " ".join(second_part)
print("Результат:", result)

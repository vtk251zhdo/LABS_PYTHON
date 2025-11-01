text = input("Введіть текст: ")

replaced_text = text.replace("а", "А")
count_replace = text.count("а")

letters = 0
for ch in text:
    if ch.isalpha():
        letters += 1

print("Текст після заміни:", replaced_text)
print("Кількість замін:", count_replace)
print("Кількість символів у рядку:", len(text))
print("Кількість літер у рядку:", letters)

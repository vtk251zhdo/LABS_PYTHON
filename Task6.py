text = input("Введіть англійський текст: ")

vowels = "aeiouyAEIOUY"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Кількість голосних у тексті:", count)

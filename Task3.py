text = input("Введіть текст українською: ").lower()
word = input("Введіть слово для підрахунку: ").lower()

for ch in ",.!?;:":
    text = text.replace(ch, "")

words = text.split()
count = 0

for w in words:
    if w == word:
        count += 1

print("Слово", word, "зустрічається", count, "раз(и)")

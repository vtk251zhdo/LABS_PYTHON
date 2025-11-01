text = input("Введіть англійський текст: ")

for ch in ",.!?;:":
    text = text.replace(ch, "")

words = text.split()
names = []

for w in words:
    if len(w) > 0 and w[0].isupper():
        names.append(w)

print("Слова, що починаються з великої літери:", names)

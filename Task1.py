text = input("Введіть текст українською (до 1000 слів): ")

if text.strip() == "":
    print("Помилка: текст порожній")
else:
    search = input("Введіть слово, з якого мають починатися інші слова: ").lower()

    words = text.replace(",", "").replace(".", "").split()
    count = 0

    for w in words:
        if w.lower().startswith(search):
            count += 1

    print("Кількість слів, що починаються з", search, ":", count)

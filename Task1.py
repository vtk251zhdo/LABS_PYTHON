text = input("Введіть текст українською (до 1000 слів): ")

if text.strip() == "":
    print("Помилка: текст порожній")
else:
    search = input("Введіть слово, з якого мають починатися або яке містяться в інших словах: ").lower()

    for ch in [",", ".", "!", "?", ":", ";", "(", ")", "[", "]", "{", "}", '"', "'"]:
        text = text.replace(ch, "")

    words = text.split()
    count = 0

    for w in words:
        if search in w.lower(): 
            count += 1

    print("Кількість слів, що містять", f"'{search}'", ":", count)

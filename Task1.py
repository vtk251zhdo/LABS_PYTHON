def task1():
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


def task2():
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


def task3():
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


def task4():
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


def task5():
    text = input("Введіть англійський текст: ")

    if not all(ch.isascii() and (ch.isalpha() or ch.isspace() or ch in ",.!?;:") for ch in text):
        print("Помилка: текст має містити лише латинські літери!")
        return 

    letter_n = input("Введіть літеру, з якої мають починатися слова: ").lower()
    letter_p = input("Введіть літеру, на яку мають закінчуватися слова: ").lower()

    if not (letter_n.isalpha() and letter_p.isalpha() and letter_n.isascii() and letter_p.isascii()):
        print("Помилка: потрібно вводити лише латинські літери!")
        return

    for ch in ",.!?;:":
        text = text.replace(ch, "")

    words = text.split()

    start_words = []
    end_words = []

    for w in words:
        if w.lower().startswith(letter_n):
            start_words.append(w)
        if w.lower().endswith(letter_p):
            end_words.append(w)

    print("Слова, що починаються з літери", letter_n, ":", start_words)
    print("Слова, що закінчуються на літеру", letter_p, ":", end_words)


def task6():
    text = input("Введіть англійський текст: ")

    if not all(ch.isascii() and (ch.isalpha() or ch.isspace() or ch in ",.!?;:") for ch in text):
        print("Помилка: текст має містити лише англійські літери!")
        return

    vowels = "aeiouyAEIOUY"
    count = 0

    for ch in text:
        if ch in vowels:
            count += 1

    print("Кількість голосних у тексті:", count)


def task7():
    text = input("Введіть англійський текст: ")

    if not all(ch.isascii() and (ch.isalpha() or ch.isspace() or ch in ",.!?;:") for ch in text):
        print("Помилка: текст має містити лише англійські літери!")
        return

    for ch in ",.!?;:":
        text = text.replace(ch, "")

    words = text.split()
    names = []

    for w in words:
        if len(w) > 0 and w[0].isupper():
            names.append(w)

    print("Слова, що починаються з великої літери:", names)


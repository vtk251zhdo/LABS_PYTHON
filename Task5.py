text = input("Введіть англійський текст: ")

letter_n = input("Введіть літеру, з якої мають починатися слова: ").lower()
letter_p = input("Введіть літеру, на яку мають закінчуватися слова: ").lower()

if not (letter_n.isalpha() and letter_p.isalpha()):
    print("Помилка: потрібно вводити лише літери")
else:
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

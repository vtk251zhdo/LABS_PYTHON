
def Task1():
    
    import os

    if not os.path.exists("numbers.txt"):
        print("Помилка: файл numbers.txt не знайдено!")
        exit()

    numbers = []

    with open("numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            value = line.strip()
            if value.lstrip("-").replace(".", "", 1).isdigit():
                numbers.append(float(value))
            else:
                print("Помилка: знайдено не число у файлі - ", value)
                exit()

    if len(numbers) == 0:
        print("Помилка: файл порожній або не містить чисел!")
        exit()

    total = sum(numbers)

    print("Сума чисел з файла:", total)

    with open("sum_numbers.txt", "w", encoding="utf-8") as f:
        f.write(str(total))
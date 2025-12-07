import os
from datetime import datetime
import time
import re
import csv

def Task1():
    
    if not os.path.exists("numbers.txt"):
        print("Помилка: файл numbers.txt не знайдено!")
        return

    numbers = []

    with open("numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            value = line.strip()
            if value.lstrip("-").replace(".", "", 1).isdigit():
                numbers.append(float(value))
            else:
                print("Помилка: знайдено не число у файлі -", value)
                return

    if len(numbers) == 0:
        print("Помилка: файл порожній або не містить чисел!")
        return

    total = sum(numbers)

    print("Сума чисел з файла:", total)

    with open("sum_numbers.txt", "w", encoding="utf-8") as f:
        f.write(str(total))


def Task2():
    
    nums = input("Введіть довільну кількість цілих чисел через пробіл: ").split()

    if len(nums) == 0:
        print("Помилка: не введено чисел!")
        return

    results = []

    for value in nums:
        if value.lstrip("-").isdigit():
            n = int(value)
            if n % 2 == 0:
                results.append(f"{n} — парне")
            else:
                results.append(f"{n} — непарне")
        else:
            print("Помилка: некоректне число - ", value)
            return

    with open("parity.txt", "w", encoding="utf-8") as f:
        for line in results:
            f.write(line + "\n")

    print("Результат записано у parity.txt")

def Task3():
    
    filename = "learning_python.txt"

    if not os.path.exists(filename):
        print("Помилка: файл learning_python.txt не знайдено!")
        return

    lines = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            text = line.strip()
            if text:
                lines.append(text)

    if len(lines) == 0:
        print("Помилка: файл порожній!")
        return

    print("Текст з файла:")
    for l in lines:
        print(l)

    sorted_lines = sorted(lines, key=len, reverse=True)

    print("\nРядки від найдовшого до найкоротшого: ")
    for l in sorted_lines:
        print(l)
        
def Task4():
    source = "learning_python.txt"

    if not os.path.exists(source):
        print("Помилка: файл learning_python.txt не знайдено!")
        return

    with open(source, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]

    if len(lines) == 0:
        print("Помилка: файл порожній!")
        return

    folder = "Task4_output"
    if not os.path.exists(folder):
        os.mkdir(folder)

    changed_file = os.path.join(folder, "learning_c.txt")
    true_file = os.path.join(folder, "true_statements.txt")
    false_file = os.path.join(folder, "false_statements.txt")

    changed_lines = [l.replace("Python", "C") for l in lines]

    with open(changed_file, "w", encoding="utf-8") as f:
        for l in changed_lines:
            f.write(l + "\n")

    print("\nЗмінені фрази:\n")

    true_list = []
    false_list = []

    for l in changed_lines:
        print(l)
        ans = input("Чи є фраза істинною для мови C? (так/ні): ").strip().lower()

        if ans == "так":
            true_list.append(l)
        elif ans == "ні":
            false_list.append(l)
        elif ans == "yes":
            false_list.append(l)
        elif ans == "no":
            false_list.append(l)
        else:
            print("Некоректна відповідь, пропуск")
            false_list.append(l)

    with open(true_file, "w", encoding="utf-8") as f:
        for l in true_list:
            f.write(l + "\n")

    with open(false_file, "w", encoding="utf-8") as f:
        for l in false_list:
            f.write(l + "\n")

    print("\nОпрацювання завершено!")
    print("Істинні твердження записано у: ", true_file)
    print("Хибні твердження записано у: ", false_file)

def Task5():
    
    filename = "guest_book.txt"

    if not os.path.exists(filename):
        created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Файл створено: " + created + "\n")
            f.write("Остання зміна: " + created + "\n\n")

    while True:
        name = input("Введіть ім'я (або 'вихід'): ").strip()

        if name.lower() == "вихід":
            print("Вихід у головне меню.")
            return

        if name == "":
            print("Помилка: ім’я порожнє!")
            continue

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        greeting = f"Вітаю, {name}! — {timestamp}"
        print(greeting)

        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        lines[1] = "Остання зміна: " + timestamp + "\n"

        with open(filename, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line)
            f.write(greeting + "\n")

def Task6():
    
    text_file = "python_text.txt"

    if not os.path.exists(text_file):
        print("Помилка: файл python_text.txt не знайдено!")
        return

    with open(text_file, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.strip():
        print("Помилка: файл порожній!")
        return

    mode = input("Оберіть режим аналізу (1 — літера, 2 — слово): ").strip()

    if mode not in ("1", "2"):
        print("Помилка: невірний режим!")
        return

    start_time = time.time()
    lower_text = text.lower()

    if mode == "1":
        target = input("Введіть літеру для пошуку: ").strip().lower()
        if len(target) != 1:
            print("Помилка: потрібно ввести одну літеру!")
            return
        total_letters = 0
        for ch in lower_text:
            if ch.isalpha():
                total_letters += 1
        count = lower_text.count(target)
        if total_letters > 0:
            frequency = count / total_letters
        else:
            frequency = 0.0
        result_type = "літера"
        total_base = total_letters
    else:
        target = input("Введіть слово для пошуку: ").strip().lower()
        if target == "":
            print("Помилка: слово порожнє!")
            return
        words = re.findall(r"\b\w+\b", lower_text)
        total_words = len(words)
        count = 0
        for w in words:
            if w == target:
                count += 1
        if total_words > 0:
            frequency = count / total_words
        else:
            frequency = 0.0
        result_type = "слово"
        total_base = total_words

    elapsed = time.time() - start_time

    print("\nРезультати аналізу: ")
    print("Тип об'єкта: ", result_type)
    print("Шукане значення: ", target)
    print("Кількість входжень у тексті: ", count)
    print("Загальна кількість елементів у базі підрахунку: ", total_base)
    print("Частота появи: ", frequency)
    print("Час, витрачений на пошук (сек): ", round(elapsed, 6))

    log_file = "analysis_log.txt"
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not os.path.exists(log_file):
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("Файл журналу створено: " + now_str + "\n")
            f.write("\n")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("Час виконання пошуку: " + now_str + "\n")
        f.write("Тип об'єкта: " + result_type + "\n")
        f.write("Шукане значення: " + target + "\n")
        f.write("Кількість входжень: " + str(count) + "\n")
        f.write("Базова кількість елементів: " + str(total_base) + "\n")
        f.write("Частота появи: " + str(frequency) + "\n")
        f.write("Час виконання (сек): " + str(round(elapsed, 6)) + "\n")
        f.write("-" * 40 + "\n")
        
def Task7():
    
    filename = "marks.lab6.csv"

    if not os.path.exists(filename):
        print("Помилка: файл marks.csv не знайдено!")
        return

    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row]

    if len(rows) == 0:
        print("Помилка: файл marks.csv порожній або некоректний!")
        return

    def parse_score(s):
        return float(s.replace(",", "."))
    
    def parse_question_value(s):
        s = s.strip()
        if s == "-" or s == "":
            return 0.0
        return float(s.replace(",", "."))
    
    def parse_duration_minutes(duration_str):
        parts = duration_str.split()
        mins = 0
        secs = 0
        for i, p in enumerate(parts):
            if p.isdigit():
                val = int(p)
                if i + 1 < len(parts) and parts[i + 1].startswith("хв"):
                    mins = val
                elif i + 1 < len(parts) and parts[i + 1].startswith("сек"):
                    secs = val
        return mins + secs / 60.0

    students = rows
    total_students = len(students)
    print("Кількість студентів, що проходили тестування: ", total_students)

    score_counts = {}
    for r in students:
        score = parse_score(r[4])
        score_counts[score] = score_counts.get(score, 0) + 1

    print("\nКількість студентів для кожної оцінки: ")
    for score, count in sorted(score_counts.items()):
        print(f"Оцінка {score}: {count} студент(ів)")

    minute_groups = {}
    for r in students:
        score = parse_score(r[4])
        minutes = int(parse_duration_minutes(r[3]))
        if minutes not in minute_groups:
            minute_groups[minutes] = []
        minute_groups[minutes].append(score)

    print("\nСередня оцінка за певний час виконання КМР: ")
    for m in sorted(minute_groups.keys()):
        scores = minute_groups[m]
        avg = sum(scores) / len(scores)
        print(f"{m} хв: середня оцінка {avg:.2f}")

    num_questions = 20
    first_q_index = 5

    correct_counts = [0] * num_questions
    for r in students:
        for i in range(num_questions):
            val = parse_question_value(r[first_q_index + i])
            if val > 0:
                correct_counts[i] += 1

    stats_filename = "marks_statistics.txt"
    with open(stats_filename, "w", encoding="utf-8") as f:
        f.write("Статистика по правильним відповідям для кожного питання:\n")
        for i in range(num_questions):
            q_name = f"student - {i + 1}"
            correct = correct_counts[i]
            wrong = total_students - correct
            pc_correct = correct / total_students * 100
            pc_wrong = wrong / total_students * 100
            f.write(f"{q_name}: правильних {pc_correct:.2f}%, неправильних {pc_wrong:.2f}%\n")

        ratios = []
        for r in students:
            score = parse_score(r[4])
            minutes_full = parse_duration_minutes(r[3])
            if minutes_full > 0:
                ratio = score / minutes_full
                ratios.append((ratio, score, r[3]))

        ratios.sort(reverse=True)
        top5 = ratios[:5]

        f.write("\nТоп-5 оцінок за співвідношенням оцінка/час:\n")
        for ratio, score, dur_str in top5:
            f.write(f"Оцінка {score}, час {dur_str}, співвідношення {ratio:.4f}\n")

    print("\nСтатистику записано у файл", stats_filename)
    

def main():
    
    while True:
        print("\nЗавдання:")
        print("1 — Завдання 1 (Сума з файла)")
        print("2 — Завдання 2 (Парність чисел)")
        print("3 — Завдання 3 (Довжина рядків)")
        print("4 — Завдання 4 (Перекладач)")
        print("5 — Завдання 5 (Вітальник)")
        print("6 — Завдання 6 (Словник про Пайтон)")
        print("7 — Завдання 7 (Довідник)")
        print("0 — Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            Task1()
        elif choice == "2":
            Task2()
        elif choice == "3":
            Task3()
        elif choice == "4":
            Task4()
        elif choice == "5":
            Task5()
        elif choice == "6":
            Task6()
        elif choice == "7":
            Task7()
        elif choice == "0":
            print("Вихід!")
            break
        else:
            print("Помилка вибору!")

main()

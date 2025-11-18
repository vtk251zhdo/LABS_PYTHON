def Task1():
        
    def is_prime(x):

        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True


    def get_primes(n):

        return [i for i in range(n + 1) if is_prime(i)]

    def format_output(primes, output_format):

        if output_format == 'list':
            return primes

        elif output_format == 'column':
            return "\n".join(str(x) for x in primes)

        elif output_format == 'count':
            return len(primes)

        else:
            return "Помилка: невідомий формат виводу!"

    def find_primes(n, output_format):

        primes = get_primes(n)
        return format_output(primes, output_format)

    while True:
        n_value = int(input("\nВведіть число N: "))

        print("Оберіть формат представлення:4")
        print("1 — список")
        print("2 — в стовпчик")
        print("3 — кількість")

        choice = input("Ваш вибір (1/2/3): ")

        if choice == "1":
            fmt = "list"
        elif choice == "2":
            fmt = "column"
        elif choice == "3":
            fmt = "count"
        else:
            print("Помилка формату!")
            continue

        result = find_primes(n_value, fmt)

        print("\nРезультат:")
        print(result)

def Task2():

    def extract_categories(item, categories, sums):

        if isinstance(item, dict):
            for key, value in item.items():
                categories.add(key)
                sums[key] = sums.get(key, 0) + value
        elif isinstance(item, list):
            for element in item:
                extract_categories(element, categories, sums)

    def analyze_nested_categories(data):

        categories = set()
        sums = {}
        extract_categories(data, categories, sums)
        return sorted(list(categories)), sums


    nested_data = [
        [
            {"офіс": 100},
            {"маркетинг": 200}
        ],
        [
            [
                {"офіс": 50},
                {"маркетинг": 150}
            ],
            {"офіс": 200}
        ],
        {"офіс": 300},
        [{"офіс": 100, "extra": 1}]
    ]

    result = analyze_nested_categories(nested_data)
    print(result)

def Task3():

    def is_valid_email(email):
        return isinstance(email, str) and "@" in email and "." in email and len(email) > 3

    def analyze_clients(clients):
        status_count = {}
        invalid_emails = []
        new_clients = []
        errors = []

        for item in clients:
            if not isinstance(item, tuple) or len(item) != 3:
                errors.append(item)
                continue

            name, status, email = item

            if not isinstance(name, str) or not isinstance(status, str) or not isinstance(email, str):
                errors.append(item)
                continue

            invalid = False

            if name.strip() == "":
                invalid = True
            if status.strip() == "":
                invalid = True
            if email.strip() == "" or not is_valid_email(email):
                invalid = True
                invalid_emails.append(email)

            if invalid:
                errors.append(item)
                continue

            status_count[status] = status_count.get(status, 0) + 1

            if status == "новий":
                new_clients.append(name)

        return {
            "status_count": status_count,
            "invalid_emails": invalid_emails,
            "new_clients": new_clients,
            "errors": errors
        }

    result = analyze_clients([
        ("Іван", "новий", "ivan@email.com"),
        ("Олена", "постійний", "olena[at]mail.com"),
        ("", "новий", "ivan@email.com"),
        ("Олена", "", "olena[at]mail.com"),
        ("Іван", "новий", ""),
        ("", "", ""),
        ("Петро", "", ""),
        "не кортеж",
        123,
        None,
        ("Олена",),
        ("Іван", "новий"),
        (123, "новий", "ivan@email.com"),
        ("Іван", 123, "ivan@email.com"),
        ("Іван", "новий", 123)
    ])

    print(result)

def Task4():

    from datetime import datetime

    def is_valid_date(date_str, date_format="%Y-%m-%d"):
        try:
            datetime.strptime(date_str, date_format)
            return True
        except (ValueError, TypeError):
            return False

    def analyze_expenses(expenses):
        category_totals = {}
        max_expense = None
        invalid_dates = []
        errors = []

        for item in expenses:
            if not isinstance(item, tuple) or len(item) != 3:
                errors.append(item)
                continue

            amount, category, date = item

            if not isinstance(amount, (int, float)):
                errors.append(item)
                continue
            if not isinstance(category, str):
                errors.append(item)
                continue
            if not is_valid_date(date):
                invalid_dates.append(date)
                errors.append(item)
                continue

            category_totals[category] = category_totals.get(category, 0) + amount

            if max_expense is None or amount > max_expense[0]:
                max_expense = item

        return {
            "category_totals": category_totals,
            "max_expense": max_expense,
            "invalid_dates": invalid_dates,
            "errors": errors
        }


    result = analyze_expenses([
        (100, "офіс", "2024-06-01"),
        (200, "маркетинг", "2024-06-02"),
        (50, "офіс", "2024-13-01"),
        (None, "маркетинг", "2024-06-02"),
        (100, None, "2024-06-01"),
        (100, "офіс", None),
        "не кортеж",
        123,
        None,
        (100, "офіс"),
        (100,),
        (100, "офіс", "2024-06-01", "extra")
    ])

    print(result)

def Task5():
        
    def filter_reports(reports, output_format, keyword):
        filtered_reports = []
        errors = []

        for item in reports:
            if not isinstance(item, tuple) or len(item) != 3:
                errors.append(item)
                continue

            title, author, fmt = item

            if not isinstance(title, str) or not isinstance(author, str) or not isinstance(fmt, str):
                errors.append(item)
                continue

            if title.strip() == "" or author.strip() == "" or fmt.strip() == "":
                errors.append(item)
                continue

            if fmt == output_format and (keyword.lower() in title.lower() or keyword.lower() in author.lower()):
                filtered_reports.append(item)

        return filtered_reports, len(filtered_reports), errors


    result = filter_reports(
        [
            ("Звіт1", "Іван Іванов", "pdf"),
            ("Звіт2", "Олена Петрівна", "docx"),
            ("", "Іван Іванов", "pdf"),
            ("Звіт3", "", "pdf"),
            ("Звіт4", "Петро Сидоров", ""),
            "не кортеж",
            123,
            None,
            ("Звіт5",),
            ("Звіт6", "Іван Іванов"),
            ("Звіт7", "Іван Іванов", 123),
        ],
        "pdf",
        "Іва"
    )

    print(result)

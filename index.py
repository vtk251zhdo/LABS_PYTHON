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
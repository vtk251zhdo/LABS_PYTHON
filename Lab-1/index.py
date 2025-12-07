a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))
d = float(input("Введіть четверте число: "))

results = [
    a + b,                   
    a - c,                    
    a * d,                 
    a / b if b != 0 else None,   
    a ** c,                     
    a // d if d != 0 else None,  
    a % b if b != 0 else None    
]

print("\nКількість елементів у списку:", len(results))

print("Парні елементи списку:")
for element in results:
    if isinstance(element, (int, float)) and element is not None:
        if element.is_integer() and int(element) % 2 == 0:
            print(int(element))

if len(results) >= 5:
    results[1], results[4] = results[4], results[1]

print("\nСписок після обміну другого і п'ятого елементів:")
print(results)

name = input("\nВведіть прізвище та ім'я: ")

print("\nАвтор лабораторної роботи:", name)
print("Висновок:")
print("1. Програма демонструє арифметичні операції над числами")
print("2. Показано роботу зі списками та умовними перевірками")
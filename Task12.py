unit = int(input("Введіть номер одиниці маси (1: кг, 2: мг, 3: г, 4: т, 5: ц): "))
mass = float(input("Введіть масу тіла в цих одиницях: "))

if unit == 1:
    mass_in_kg = mass
elif unit == 2:
    mass_in_kg = mass / 1_000_000
elif unit == 3:
    mass_in_kg = mass / 1_000
elif unit == 4:
    mass_in_kg = mass * 1_000
elif unit == 5:
    mass_in_kg = mass * 100
else:
    mass_in_kg = None
    print("Помилка: введіть число від 1 до 5")

if mass_in_kg is not None:
    print(f"Маса тіла у кілограмах: {mass_in_kg} кг")

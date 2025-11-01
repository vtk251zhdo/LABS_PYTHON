def get_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолій"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Риби"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телець"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "Близнюки"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Діва"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Терези"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
        return "Скорпіон"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "Стрілець"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козоріг"
    else:
        return "Некоректна дата"

day = int(input("Введіть день: "))
month = int(input("Введіть місяць: "))

zodiac_sign = get_zodiac_sign(day, month)
print(f"Знак зодіаку для дати {day}.{month}: {zodiac_sign}")

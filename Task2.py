purchase_amount = float(input("Введіть суму покупки: "))

discount = 0
if purchase_amount > 1000:
    discount = 0.05
elif purchase_amount > 500:
    discount = 0.03

discounted_price = purchase_amount * (1 - discount)

print(f"Початкова сума: {purchase_amount} грн")
print(f"Знижка: {discount * 100}%")
print(f"Сума до сплати: {discounted_price:.2f} грн")
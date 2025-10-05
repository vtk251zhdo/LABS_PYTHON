a = float(input("Enter the first number (integer or fractional): "))
b = float(input("Enter the second number (integer or fractional): "))
c = float(input("Enter the third number (integer or fractional): "))
d = float(input("Enter the fourth number (integer or fractional): "))

results = [
    a + b,  
    a - c,
    b * d,  
    a / b if b != 0 else "Division by zero",
    c ** d,  
    a // b if b != 0 else "Integer division by zero",  
    a % b if b != 0 else "Modulo by zero"  
]

print("Number of elements in the list:", len(results))
print("Even elements in the list:")
for element in results:
    if isinstance(element, (int, float)) and element % 2 == 0:
        print(element)
if len(results) >= 5:
    results[1], results[4] = results[4], results[1]
print("List after swapping second and fifth elements:", results)

name = input("Enter your last name and first name: ")
print("\nAuthor of this lab work:", name)
print("Conclusion:")
print("1. The program demonstrates basic arithmetic operations.")
print("2. It shows how to manipulate lists and handle user input.")
print("3. The tasks were completed successfully.")
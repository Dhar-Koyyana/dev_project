print("🔢 Welcome To Calculator App! ➕ ➖ ✖️ ➗")
print("\nChoose your operation:")
print("0. All Operations")
print("1. Addition (➕)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Modulo (%)")
print("5. Exit ❌")

def perform_operation(option, num1, num2):
    if option == 0:
        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} * {num2} = {num1 * num2}")
        print(f"{num1} % {num2} = {num1 % num2}")
    elif option == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif option == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif option == 3:
        print(f"{num1} * {num2} = {num1 * num2}")
    elif option == 4:
        print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("❌ Please enter a valid option.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

while True:
    option = int(input("Enter your choice: "))

    if option == 5:
        print("🙏 THANKS FOR CHOOSING CALCULATOR 🔚")
        break

    perform_operation(option, num1, num2)


def addition():
    print("Easy way to sum up!")
    first_number = int(input("What is your first number? "))
    second_number = int(input("What is your second number? "))
    result = first_number + second_number
    print(f"The result is: {result}")

def subtraction():
    print("Subtraction")
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    result = first_number - second_number
    print(f"The result is: {result}")

def multiplication():
    print("Multiplication")
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    result = first_number * second_number
    print(f"The result is: {result}")

def division():
    print("Division")
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    if second_number != 0:
        result = first_number / second_number
        print(f"The result is: {result}")
    else:
        print("Error: Cannot divide by zero")

# Main calculator function
def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == '1':
        addition()
    elif choice == '2':
        subtraction()
    elif choice == '3':
        multiplication()
    elif choice == '4':
        division()
    else:
        print("Invalid input")

# This will loop to allow multiple operations until the user decides to quit
while True:
    calculator()
    another = input("Do you want to perform another operation? (yes/no): ").lower()
    if another != 'yes':
        break
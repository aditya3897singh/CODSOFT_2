#-----------------------------------  SIMPLE CALCULATOR -----------------------------------------

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))  #taking opernads from user

print("\nChoose an operation: +, -, *, /")
op = input("Enter your choice: ")     # deciding operator

match op:   # performing calculation
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero!")
    case _:
        print("Invalid operation!")
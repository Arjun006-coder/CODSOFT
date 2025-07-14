def calculator():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Choose operation: +  -  *  /")
        op = input("Enter operation: ")

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Cannot divide by zero!")
                return
        else:
            print("Invalid operation!")
            return

        print(f"Result: {result}")
    except ValueError:
        print("Invalid number input!")

calculator()

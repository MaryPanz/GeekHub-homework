def calculate():
    try:
        num1 = int(input("Print a number: "))
        num2 = int(input("Print a number: "))
        op = input("Print an operator: ")
        operators = ["+", "-", "*", "/", "%", "//", "**"]
        if op not in operators:
            print("Something went wrong!")
        else:
            print(f"{num1} {op} {num2} =", end = " ")
            if op == "+":
                print(num1 + num2)
            elif op == "-":
                print(num1 - num2)
            elif op == "*":
                print(num1 * num2)
            elif op == "/":
                print(num1 / num2)
            elif op == "//":
                print(num1 // num2)
            elif op == "%":
                print(num1 % num2)
            elif op == "**":
                print(num1 ** num2)
    except ValueError:
        print("You didn't type a correct number!")
        
calculate()
    

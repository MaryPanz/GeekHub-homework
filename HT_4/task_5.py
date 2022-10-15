"""
5. Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1 функцiя, яка приймає 3 аргументи - один з яких операцiя, яку зробити! 
Аргументи брати від юзера (можна по одному - окремо 2, окремо +, окремо 2; можна всі разом - типу 2 + 2). 
Операції що мають бути присутні: +, -, *, /, %, //, **. 
Не забудьте протестувати з різними значеннями на предмет помилок!"""

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
    

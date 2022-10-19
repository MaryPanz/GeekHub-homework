"""5. Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його."""

n = int(input("Number: "))

def fibonnachi(n):
    num1, num2 = 0, 1
    count = 0
    if n > 1:
        print("Fibonacci:", end = " ")
        while count <= n:
            print(count, end = " ")
            num1 = num2
            num2 = count
            count = num1 + num2
    elif n < 0:
        print("Your number should be bigger than 0!")
    else:
        print(num1)
    
fibonnachi(n)

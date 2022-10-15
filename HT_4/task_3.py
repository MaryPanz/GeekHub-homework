"""3. Користувач вводить змінні "x" та "y" з довільними цифровими значеннями. 
Створіть просту умовну конструкцію (звiсно вона повинна бути в тiлi ф-цiї), 
під час виконання якої буде перевірятися рівність змінних "x" та "y" та у випадку нерівності - виводити ще і різницю.
    Повинні працювати такі умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      відповідь - "х дорівнює y"  """

def compare_numbers():
    x = int(input("1.Print a number: "))
    y = int(input("2.Print a number: "))
    
    if x > y:
        z = x - y
        return(f"Answer: {x} is bigger than {y} by {z}.")
    elif x < y:
        z = y - x
        return(f"Answer: {x} is smaller than {y} by {z}.")
    else:
        return(f"Answer: The numbers {x} and {y} are equal!")
    
print(compare_numbers())

"""Write a script which accepts a decimal number from user and converts it to hexadecimal."""

my_decimal = input("Please enter a decimal number: ")

if my_decimal.isdecimal():
    my_hex = hex(int(my_decimal))
    print("This is a hexadecimal from your decimal:", my_hex)
else:
    print("That was not a decimal number!")

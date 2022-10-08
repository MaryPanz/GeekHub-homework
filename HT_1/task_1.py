"""Write a script which accepts a sequence of comma-separated numbers from user and generates a list and a tuple with those numbers."""

# splits a str into a list
print("This is my example: 1,3,5")

my_numbers = input("Please, print numbers separated by commas: ").split(",")

print("This is my list: ", my_numbers)
print("This is my tuple: ", tuple(my_numbers))

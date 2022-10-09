"""Write a script which accepts a <number> from user and then <number> times asks user for string input.
At the end script must print out result of concatenating all <number> strings."""

my_number = int(input("Please, print one number: "))
my_sum = ""
for i in range(my_number):
    my_sum += "".join(input("Type your sentence here: "))
print(f"This is the sum of all your sentences: {my_sum}")

"""Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers."""

my_number = int(input("Please, print one number: "))
my_sum = 0
for i in range(my_number + 1):
    my_sum = my_sum + i
print(f"This is my sum: {my_sum}!")

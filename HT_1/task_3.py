"""Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers."""

my_number = int(input("Please, print one number: "))
my_sum = sum(range(my_number + 1))
print(my_sum)

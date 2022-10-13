"""Write a script that will run through a list of tuples and replace the last value for each tuple. 
The list of tuples can be hardcoded. The "replacement" value is entered by user. 
The number of elements in the tuples must be different."""

my_tuple_list = [(1,2,3), (4,5), (6,7,8,9)]

my_value = input("Please, write your value: ")
my_new_list = [i[:-1] + (my_value,) for i in my_tuple_list if i]

print("This is my new list: ", my_new_list)

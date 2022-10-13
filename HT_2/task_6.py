"""Write a script to get the maximum and minimum VALUE in a dictionary."""
my_dict = {"cookies": 25, "bread": 1, "carrots": 3, "cakes": 2}
only_value = my_dict.values()
print("This is my dictionary:", my_dict)
print("This is the maximum value:", (max(only_value)))
print("This is the minimum value:", (min(only_value)))


"""Write a script to check whether a value from user input is contained in a group of values.
    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
         [1, 2, 'u', 'a', 4, True] --> 5 --> False"""

my_value = input("Type a value: ")
my_list0 = [1, 2, 3, "u", "a", True]

my_str = ""
my_str = "".join([str(i) for i in my_list0])
print(my_value in my_str)

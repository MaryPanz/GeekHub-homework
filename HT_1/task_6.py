
"""Write a script to check whether a value from user input is contained in a group of values.
    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
         [1, 2, 'u', 'a', 4, True] --> 5 --> False"""
         
my_value = ""
my_value = input("Type a value: ")
my_list0 = [1, 2, 3, "u", "a", True]

# numbers
if my_value.isdecimal():
    int_value = (int(my_value))
    print(int_value in my_list0)
# letters
elif my_value in my_list0:
    print(my_value in my_list0)
# T/F
elif (my_value == str(my_list0[5])):
    print(True)
else:
    print(False)

"""Write a script to concatenate all elements in a list into a string and print it. 
List must include both strings and integers and must be hardcoded."""

my_list = ["String1", 55, "String2", 2, 4]
print(f"This is my list: {my_list}")

my_str = ""
for i in my_list:
    my_str += str(i)
    
print(f"This is my new string: {my_str}")

"""Write a script to remove values duplicates from dictionary. 
Feel free to hardcode your dictionary."""
my_dict = {"cat": 5, "dog": 2, "rabbit": 2, "cows": 5} 
new_dict = {}
my_list = []
for key, value in my_dict.items():
    if value not in my_list:
        my_list.append(value)
        new_dict[key] = value
print(new_dict)

"""Write a script to remove values duplicates from dictionary. 
Feel free to hardcode your dictionary."""
my_dict = {"cat": 5, "dog": 2, "rabbit": 2, "cows": 5} 
new_dict = {}

for key, value in my_dict.items():
    if value not in new_dict.values():
        new_dict[key] = value
print(new_dict)

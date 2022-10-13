"""Write a script which accepts a <number>(int) from user and generates dictionary in range <number> where key is <number> and value is <number>*<number>
    e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}"""
my_number = int(input("Type a number: "))
my_dict = {}
for i in range(my_number, my_number + 4):
    my_dict[i] = i**2

print("This is my dictionary:", my_dict)

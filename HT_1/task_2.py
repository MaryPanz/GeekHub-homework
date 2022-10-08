"""Write a script which accepts two sequences of comma-separated colors from user. 
Then print out a set containing all the colors from color_list_1 which are not present in color_list_2."""

print("Please print colors as in red,blue,orange etc")
my_colors0 = set(input("Print colors 1: "))
my_colors1 = set(input("Print colors 2: "))

color_diff = my_colors0.difference(my_colors1)
print("This is the unique color set from colors 1:", color_diff)


my_tuple_list = [(1,2,3), (4,5), (6,7,8,9)]

my_value = input("Please, write your value: ")

print("This is my new list: ", [i[:-1] + (my_value,) for i in my_tuple_list])

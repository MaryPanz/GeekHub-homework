"""Write a script to remove empty elements from a list."""
my_list = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
new_list = list(filter(None, my_list))
print("This is my new list: ", new_list)

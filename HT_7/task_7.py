my_list1 = [1,2,3,4,5]
my_list2 = [3,4,6,7,8]

def merge_list(my_list1, my_list2):
    result = [element for element in my_list1 if element not in my_list2] 
    print(result)

merge_list(my_list1, my_list2)

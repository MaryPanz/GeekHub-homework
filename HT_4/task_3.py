def compare_numbers():
    x = int(input("1.Print a number: "))
    y = int(input("2.Print a number: "))
    
    if x > y:
        z = x - y
        return(f"Answer: {x} is bigger than {y} by {z}.")
    elif x < y:
        z = y - x
        return(f"Answer: {x} is smaller than {y} by {z}.")
    else:
        return(f"Answer: The numbers {x} and {y} are equal!")
    
print(compare_numbers())

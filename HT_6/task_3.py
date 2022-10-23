def status():
    
    my_list = [["Melissa", "qwertrty5tY"], ["Angelina", "asdfghj567"], ["Bob", "qwertyMJU"], ["qwe", ""]]
    
    for i in range(len(my_list)):
        name = my_list[i][0]
        password = my_list[i][1]
        print("Name:", name)
        print("Password:", password)
        print("Status: ", end = "")
        
        if len(name) > 50:
            print("The name must be smaller than 50 symbols\n")
        elif len(name) < 3:
            print("The name must be bigger than 2 symbols\n")
        elif len(password) < 8:
            print("The password can't be less than 8 digits\n")
        elif not any(i.isdigit() for i in password):
            print("The password should have a number\n")
        elif not any(i.isupper() for i in password):
            print("The password should have an uppercase letter\n")
        else:
            print("Valid!\n")
        
status()
    

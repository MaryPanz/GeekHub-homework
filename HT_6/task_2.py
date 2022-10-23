name = input("Name: ")
password = input("Password: ")


def validate(name, password):
    
    if len(name) > 50:
        print("The name must be smaller than 50 symbols")
    elif len(name) < 3:
        print("The name must be bigger than 2 symbols")
    elif len(password) < 8:
        print("The password can't be less than 8 digits")
    elif not any(i.isdigit() for i in password):
        print("The password should have a number")
    elif not any(i.isupper() for i in password):
        print("The password should have an uppercase letter")
    else:
        print("Valid!")
    
validate(name, password)

"""Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параметрів не відповідає вимогам - породити виключення із відповідним текстом."""


class LoginNameError(Exception):
    pass


class LoginPassError(Exception):
    pass


name = input("Name: ")
password = input("Password: ")


def validate(name, password):

    try:
        if len(name) < 3 or len(name) > 50:
            raise LoginNameError
        elif len(password) < 8:
            raise LoginPassError
        elif not any(i.isdigit() for i in password):
            raise LoginPassError
        elif not any(i.isupper() for i in password):
            raise LoginPassError
        else:
            print("Valid!\n")

    except LoginNameError:
        print("The name must be from 3-50 symbols\n")
    except LoginPassError:
        print("The password can't be less than 8 digits, should have a number and an uppercase letter\n")


validate(name, password)





"""Without try/except

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
"""

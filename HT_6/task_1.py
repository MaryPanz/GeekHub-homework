"""1. Створіть функцію, всередині якої будуть записано СПИСОК із п'яти користувачів (ім'я та пароль). 
Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - 
необов'язковий параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено правильну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція повертає False
        якщо silent == False - породжується виключення LoginException (його також треба створити =))"""

class LoginException(Exception):
    pass


username = input("Your username: ")
password = input("Your password: ")


def my_users(username, password, silent=False):
    my_users_list = [["david", "1234"], ["kate", "2345"], ["leo", "1234"], ["bob", "4342"], ["emily", "5454"]]
    user_pass = [username, password]

    try:
        if user_pass in my_users_list:
            silent = True
            if silent:
                print(False)
        else:
            raise LoginException
    except LoginException:
        print("Your username/password is incorrect!")


my_users(username, password, silent=False)

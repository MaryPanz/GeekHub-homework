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
            return True
        else:
            if silent == True:
                return False
            else:
                raise LoginException("Your username/password is incorrect!")
    except LoginException as e:
        return(e)


print(my_users(username, password, silent=False))

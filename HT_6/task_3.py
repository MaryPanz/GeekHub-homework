""". На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані 
   і надрукує для кожної пари значень відповідне повідомлення, наприклад: 
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK   P.S. Не забудьте використати блок try/except ;)"""



class LoginNameError(Exception):
    pass


class LoginPassError(Exception):
    pass


def status():


    my_list = [["Melissa", "qwertrty5tY"], ["Angelina", "asdfghj567"], ["Bob", "qwertyMJU"], ["qy", ""]]

    for i in range(len(my_list)):
        name = my_list[i][0]
        password = my_list[i][1]
        print("Name:", name)
        print("Password:", password)
        print("Status: ",end="")

        
        try:
            if len(name) < 3 or len(name) > 50:
                raise LoginNameError("The name must be from 3-50 symbols\n")
            elif len(password) < 8:
                raise LoginPassError("The password must be bigger than 8 symbols\n")
            elif not any(i.isdigit() for i in password):
                raise LoginPassError("The password must have a number\n")
            elif not any(i.isupper() for i in password):
                raise LoginPassError("The password must have an uppercase letter\n")
            else:
                print("Valid!\n")

        except LoginNameError as ex:
            print(ex)
        except LoginPassError as ex:
            print(ex)

status()

class Error(Exception):
    pass
    
class LoginException(Error):
    pass
  

username = input("Your username: ")
password = (input("Your password: "))


def my_users(username, password, silent = False):
    
    my_users_list = [["david", "1234"], ["kate", "2345"], ["leo", "1234"], ["bob", "4342"], ["emily", "5454"]]
    user_pass = [username, password]
    
    try:    
        for i in range(len(my_users_list)):
            if(my_users_list[i] == user_pass):
                silent = True
                print(silent)
                break
        else:
            raise LoginException
            
    except LoginException:
        print("Your username/password is incorrect!")
    
            
(my_users(username, password, silent = False))

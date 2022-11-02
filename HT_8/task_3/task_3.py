# To withdraw enter 100, not -100. Numbers < 0 will show a mistake.


import csv
import json


def main():

    
    name = input("Name: ")
    password = input("Password: ")
    print(f"Welcome, {name}!\n")

    while True:
        try:
            if validate(name, password) == True:
                a = action()
                if a == 1:
                    balance(a, name)
                elif a == 2:
                    amount = top_up(name)
                    history_transaction(name, amount)
                elif a == 3:
                    amount = withdraw(name)
                    history_transaction(name, amount)
                elif a == 4:
                    print("Goodbye!")
                    break
                else:
                    print("Wrong number!")
            else:
                print("The account does not exist!")  
                break
        except ValueError:
            print("The value is wrong!")
        except FileNotFoundError:
            print("Something!")
            break



def validate(name, password):
    
        
    with open("users.csv", "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:

            if row[0] == name and row[1] == password:
                login = True
                break
            else:
                login = False 
    if login:
        return True
    else:
        return False
    


def action():
    
   
    print("1 Balance")
    print("2 Top up")
    print("3 Withdraw")
    print("4 Exit")

    number = int(input("Number: "))

    if number == 1:
        return 1
    elif number == 2:
        return 2
    elif number == 3:
        return 3
    elif number == 4:
        return 4
    else:
        return 5
     

def balance(a, name):


    with open(f"{name}_balance.txt") as txt_file:
        lines = txt_file.readlines()
        print(f"Your balance is {lines[0]}$\n")


def top_up(name):
    

    with open(f"{name}_balance.txt", "r+") as txt_file:
        lines = txt_file.readlines()
        amount = int(input("Enter amount: "))

        if amount < 0:
            print("The amount too small!")
        else:
            new_balance = int(lines[0]) + amount
            print("Your balance is:", new_balance)
            txt_file.seek(0)
            txt_file.write(str(new_balance))
            return amount 
           
    
def withdraw(name):


    with open(f"{name}_balance.txt", "r") as txt_file:
        lines = txt_file.readlines()
        amount = int(input("Enter amount: "))
        if amount <= int(lines[0]):
            if amount > 0:

                new_balance = int(lines[0]) - amount
                print("Your balance is:", new_balance)
                txt_file.seek(0)

                with open(f"{name}_balance.txt", "w") as txt_file:

                    txt_file.write(str(new_balance))
                    return amount
            else:
                print("The amount is less than 0!")
                    
        else:
            print("The amount is bigger than your balance!")

     
def history_transaction(name, amount):


    with open(f"{name}_transaction.json", "r") as js_file:
        
        data = json.load(js_file)
        data.append({name: amount})
            
    with open(f"{name}_transaction.json", "w") as j_file:
        json.dump(data, j_file)


if __name__ == "__main__":
    main()

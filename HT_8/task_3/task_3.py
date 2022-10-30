import csv
import json


def main():


    while True:
        try:
            name = input("Name: ")
            password = input("Password: ")
            if validate(name, password) == True:
                print(f"Welcome {name}!")
                a = action()
                t_w = change_balance(a,name)
                top_up(t_w, name)
                withdraw(t_w, name)
                break

            else:
                print("Try!")
        except ValueError:
            print("Somthing went wrong")


def validate(name,password):


    try:
        

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
    except FileNotFoundError:
        print("File does not exist!")


def action():
    print("1 Balance")
    print("2 Top up/Withdraw")
    print("3 Exit")

    number = int(input("Number: "))

    if number == 1:
        return 1
    elif number == 2:
        return 2
        
    else:
        print("Exit!")
        return 3


def balance(a, name):
    if a == 1:
        print("Your balance is: ")
        try:
            with open(f"{name}_balance.txt") as txt_file:
                lines = txt_file.readlines()
                print(lines[0])

        except FileNotFoundError:
            print("Text file does not exist!")


    else:
        return False

def change_balance(a, name):
    if a == 2:
        t_w = int(input("For top up press 1, for withdraw press 2: "))
        return t_w
    else:
        return False

def top_up(t_w, name):
    if t_w == 1:

        try:
            with open(f"{name}_balance.txt", "r+") as txt_file:
                lines = txt_file.readlines()
                amount = int(input("Enter amount: "))
                new_balance = int(lines[0]) + amount
                print("Your balance is:", new_balance)
                txt_file.seek(0)
                txt_file.write(str(new_balance))
        except FileNotFoundError:
            print("Text file does not exist!")        
    else:
        return False

def withdraw(t_w, name):

    if t_w == 2:
        try:
            with open(f"{name}_balance.txt", "r+") as txt_file:
                lines = txt_file.readlines()
                amount = int(input("Enter amount: "))
                if amount < int(lines[0]):

                    new_balance = int(lines[0]) - amount
                    print("Your balance is:", new_balance)
                    txt_file.seek(0)
                    txt_file.write(str(new_balance))
                else:
                    print("The amount is too big!")
    
        except FileNotFoundError:
            print("Text file does not exist!")


  






if __name__ == "__main__":
    main()

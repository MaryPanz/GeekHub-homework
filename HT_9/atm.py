# admin 1111
# bob 1234


import sqlite3
from datetime import datetime


def main():


    connection = sqlite3.connect("a.db")
    cursor = connection.cursor()
    user = login(cursor)
    print("Welcome!")

    while True:

        try:
            connection = sqlite3.connect("a.db")
            cursor = connection.cursor()
            action_ = action()
            if action_ == 1:
                balance(user,cursor)
            elif action_ == 2:
                top_up(user,cursor,connection)
                print("Your balance is: ")
                balance(user,cursor)
            elif action_ == 3:
                withdraw(user,cursor,connection)
                balance(user,cursor)
            elif action_ == 4:
                print("Goodbye!")
                break
            elif action_ == 5:
                if user == "admin":
                    print("Welcome, administartor!")
                    while True:
                        act = admin_action()
                        if act == 1:
                            admin_balance(cursor)
                        elif act == 2:
                            admin_money_topup(cursor,connection)
                        elif act == 3:
                            banknote_count(cursor)
                        elif act == 4:
                            admin_money_withdraw(cursor,connection)
                        elif act == 5:
                            print("Leaving the admin menu.")
                            break
                        else:
                            print("Wrong action!")
                else:
                    print("Sorry, you cannot use this option")
            else:
                print("Wrong number entered!")

            cursor.close()
            connection.close()
        except NameError:
            print("The value entered is wrong!")
        except ValueError:
            print("The entered value is wrong")


def login(cursor):


    while True:
        user = input("Username: ")
        password = input("Password: ")
        print("Connecting...")
        result = cursor.execute("SELECT * FROM bank WHERE name = ? AND password = ?", (user,password,))
        if len(result.fetchall()) > 0:
            print("Connected!")
            return user
        else:
            print("No such user!")


def action():


    print("1 Balance")
    print("2 Top up")
    print("3 Withdraw")
    print("4 Exit")
    print("5 Admin")
    number = int(input("Number: "))
    return number


def balance(user,cursor):


    cursor.execute("SELECT balance FROM bank WHERE name = ?", (user,))
    result = cursor.fetchone()
    result = "".join(map(str, result))
    print(result)


def top_up(user,cursor,connection):


    amount = int(input("Enter amount: "))
    if amount < 0:
        print("The amount is too small!")
    elif amount > 0:
        cursor.execute("SELECT balance FROM bank WHERE name = ?", (user,))
        result = cursor.fetchone()
        result = int("".join(map(str, result))) + amount
        if result % 10 == 0:
            print("Transaction completed!")
            cursor.execute("UPDATE bank SET balance = ? WHERE name = ?", (result,user,))
            connection.commit()
            # update total bank balance
            cursor.execute("SELECT total FROM banknotes")
            total = cursor.fetchone()
            new_total = int("".join(map(str, total))) + amount
            cursor.execute(f"UPDATE banknotes SET TOTAL = ? ", (new_total,))
            connection.commit()
            flag = "+"
            history_transaction(user, amount, connection, flag)
        else:
            result = result - 5
            cursor.execute("UPDATE bank SET balance = ? WHERE name = ?", (result,user,))
            # update total bank balance
            cursor.execute("SELECT total FROM banknotes")
            total = cursor.fetchone()
            new_total = int("".join(map(str, total))) + result
            cursor.execute(f"UPDATE banknotes SET TOTAL = ? ", (new_total,))
            connection.commit()
            print(result)
            print("Change: 5")
            return amount
    else:
        print("You entered a wrong value!")


def withdraw(user,cursor,connection):


    cursor.execute("SELECT balance FROM bank WHERE name = ?", (user,))
    current_balance = cursor.fetchone()
    current_balance  = int(str(current_balance ).strip(",()"))
    print("Your available balance is: %d" % current_balance)
    amount = int(input("Enter amount: "))
    if amount <= current_balance:
        if amount > 0:

            new_balance = current_balance  - amount
            print("Your balance now is: %d" % new_balance)
            print("Transaction completed!")
            cursor.execute("UPDATE bank SET balance = ? WHERE name = ?", (new_balance,user,))
            connection.commit()
            # update total bank balance
            cursor.execute("SELECT total FROM banknotes")
            total = cursor.fetchone()
            new_total = int("".join(map(str, total))) - amount
            cursor.execute(f"UPDATE banknotes SET TOTAL = ? ", (new_total,))
            connection.commit()
            flag = "-"
            history_transaction(user, amount, connection, flag)
        else:
            print("The amount is less than 0!")
    else:
        print("The amount is bigger than your balance!")


def admin_action():


    print("1 Atm Balance")
    print("2 Top up by banknotes")
    print("3 Check amount of a certain banknote")
    print("4 Withdraw banknotes")
    print("5 Exit admin menu")
    number = int(input("Number: "))
    return number


def admin_balance(cursor):


    cursor.execute("SELECT total FROM banknotes")
    total = cursor.fetchone()
    new_total = "".join(map(str, total))
    print(f"The total bank amount is {new_total}")


def admin_money_topup(cursor,connection):


    print("Top up for separate banknotes")
    banknote = int(input("You can type 10/20/50/100/200/500/1000: "))
    amount = int(input("How many? "))
    banknotes = [10,20,50,100,200,500,1000]
    if banknote < 0:
        print("The amount is too small!")
    elif banknote in banknotes:
        money = banknote * amount
        cursor.execute(f"SELECT N{banknote} FROM banknotes")
        old_banknote = cursor.fetchone()
        new_b = int("".join(map(str, old_banknote))) + amount
        cursor.execute("SELECT total FROM banknotes")
        total = cursor.fetchone()
        new_total = int("".join(map(str, total))) + money
        #updates certain banknote count and total
        cursor.execute(f"UPDATE banknotes SET N{banknote} = ?, TOTAL = ? ", (new_b,new_total,))
        connection.commit()
        print(f"{banknote} times {amount} topped up. Total atm amount: {new_total}")
    else:
        print("Wrong amount entered!")


def admin_money_withdraw(cursor,connection):
    print("Withdraw for separate banknotes")
    banknote = int(input("You can type 10/20/50/100/200/500/1000: "))
    amount = int(input("How many? "))
    cursor.execute("SELECT total FROM banknotes")
    total = cursor.fetchone()
    money = banknote * amount
    banknotes = [10,20,50,100,200,500,1000]

    if banknote < 0:
        print("The amount is too small!")
    elif int("".join(map(str, total))) < money:
        print("Not enough money to withdraw!")
    elif banknote in banknotes:
        cursor.execute(f"SELECT N{banknote} FROM banknotes")
        old_banknote = cursor.fetchone()
        new_b = int("".join(map(str, old_banknote))) - amount
        new_total = int("".join(map(str, total))) - money
        #updates certain banknote count and total
        cursor.execute(f"UPDATE banknotes SET N{banknote} = ?, TOTAL = ? ", (new_b,new_total,))
        connection.commit()
        print(f"{banknote} times {amount} withdrawn. Total atm amount: {new_total}")
    else:
        print("Wrong amount entered!")


def banknote_count(cursor):


    banknote = int(input("You can type 10/20/50/100/200/500/1000: "))

    if banknote < 0:
        print("The amount is too small!")
    elif any(banknote % n == 0 for n in (10,20,50,100,500,1000)):
        cursor.execute(f"SELECT N{banknote} FROM banknotes")
        old_banknote = cursor.fetchone()
        old_banknote = "".join(map(str, old_banknote))
        print(f"The amount of {banknote}s is {old_banknote} banknotes total")
    else:
        print("You entered a wrong value!")


def history_transaction(user, amount, connection,flag):


    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    connection.execute("INSERT INTO transactions(NAME,FLAG,AMOUNT,TIME) \
    VALUES (?,?,?,?)", (user,flag,amount,dt_string))
    connection.commit()
    return True
    #cursor.execute("select * from transactions")
    #results = cursor.fetchall()
    #print(results)

if __name__ == "__main__":
    main()

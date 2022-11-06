# admin 1111
# bob 1234


import sqlite3


def main():


        connection = sqlite3.connect("my_bank.db")
        cursor = connection.cursor()
        connection2 = sqlite3.connect("banknotes.db")
        cursor2 = connection2.cursor()

        user = login(cursor)
        print("Welcome!")
        while True:
            try:
                connection = sqlite3.connect("my_bank.db")
                cursor = connection.cursor()
                connection2 = sqlite3.connect("banknotes.db")
                cursor2 = connection2.cursor()


                a = action()
                if a == 1:
                    balance(user,cursor)
                elif a == 2:
                    top_up(user,cursor,connection,cursor2,connection2)
                    print("Your balance is: ")
                    balance(user,cursor)
                elif a == 3:
                    withdraw(user,cursor,connection)
                    print("Your balance is: ")
                    balance(user,cursor)
                elif a == 4:
                    print("Goodbye!")
                    break
                elif a == 5:
                    if user == "admin":
                        print("Welcome, administartor!")
                        act = admin_action()
                        if act == 1:
                            admin_balance(cursor2)
                        elif act == 2:
                            admin_money_topup(cursor2,connection2)
                        elif act == 3:
                            banknote_count(cursor2,connection2)
                        else:
                            print("Wrong action!")
                    else:
                        print("Sorry, you cannot use this option")
                else:
                    print("Wrong number entered!")

                cursor.close()
                cursor2.close()
                connection.close()
                connection2.close()
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
        if (len(result.fetchall()) > 0):
            print("Connected!")
            return(user)
            break
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
    result = str(result).strip(",()")
    print(result)


def top_up(user,cursor,connection,cursor2,connection2):


    amount = int(input("Enter amount: "))
    if amount < 0:
        print("The amount too small!")
    elif amount > 0:  
        cursor.execute("SELECT balance FROM bank WHERE name = ?", (user,))
        result = cursor.fetchone()
        result = int(str(result).strip(",()")) + amount
        if result % 10 == 0:
            print("Transaction completed!")
            cursor.execute("UPDATE bank SET balance = ? WHERE name = ?", (result,user,))
            connection.commit()

            # update total bank balance
            cursor2.execute("SELECT total FROM banknotes")
            total = cursor2.fetchone()
            new_total = int(str(total).strip(",()")) + amount
            cursor2.execute(f"UPDATE banknotes SET TOTAL = ? ", (new_total,))
            connection2.commit()

        else:
            result = result - 5
            cursor.execute("UPDATE bank SET balance = ? WHERE name = ?", (result,user,))
            # update total bank balance
            cursor2.execute("SELECT total FROM banknotes")
            total = cursor2.fetchone()
            new_total = int(str(total).strip(",()")) + result
            cursor2.execute(f"UPDATE banknotes SET TOTAL = ? ", (new_total,))
            connection2.commit()
            print(result)
            print("Change: 5")
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

            
            # update total bank balance
            cursor.execute("SELECT bankbalance FROM bank WHERE name = 'admin'")
            bank_balance = cursor.fetchone()
            newbalance = int(str(bank_balance).strip(",()")) - amount
            cursor.execute("UPDATE bank SET bankbalance = ? WHERE name = 'admin'", (newbalance,))
            connection.commit()
        else:
            print("The amount is less than 0!")
                    
    else:
        print("The amount is bigger than your balance!")
        

def admin_action():
    print("1 Atm Balance")
    print("2 Top up by banknotes")
    print("3 Check amount of a certain banknote")
    number = int(input("Number: "))
    return number


def admin_balance(cursor2):

  
    cursor2.execute("SELECT total FROM banknotes")
    total = cursor2.fetchone()
    new_total = int(str(total).strip(",()"))
    print(f"The total bank amount is {new_total}")


def admin_money_topup(cursor2,connection2):
  
  
    print("Top up for separate banknotes")
    banknote = int(input("You can type 10/20/50/100/200/500/1000: "))
    amount = int(input("How many? "))

    if banknote < 0:
        print("The amount is too small!")
    elif any(banknote % n == 0 for n in (10,20,50,100,500,1000)):
        money = banknote * amount
        cursor2.execute(f"SELECT N{banknote} FROM banknotes")
        old_banknote = cursor2.fetchone()
        new_b = int(str(old_banknote).strip(",()")) + amount
        cursor2.execute("SELECT total FROM banknotes")
        total = cursor2.fetchone()
        new_total = int(str(total).strip(",()")) + money
        
        #updates certain banknote count and total
        cursor2.execute(f"UPDATE banknotes SET N{banknote} = ?, TOTAL = ? ", (new_b,new_total,))
        connection2.commit()
        print(f"{banknote} times {amount} topped up. Total atm amount: {new_total}")

    else:
        print("Wrong amount entered!")

def banknote_count(cursor2,connection2):
  
  
    banknote = int(input("You can type 10/20/50/100/200/500/1000: "))

    if banknote < 0:
        print("The amount is too small!")
    elif any(banknote % n == 0 for n in (10,20,50,100,500,1000)):
        cursor2.execute(f"SELECT N{banknote} FROM banknotes")
        old_banknote = cursor2.fetchone()
        old_banknote = int(str(old_banknote).strip(",()"))
        print(f"The amount of {banknote}s is {old_banknote} banknotes total")
    else:
        print("You entered a wrong value!")


    
if __name__ == "__main__":
    main()

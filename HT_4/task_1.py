n = int(input("Please, print a number from 1-12: "))

def write_season(n):
    if n > 12 or n < 1:
        print("Wrong number!")
    else:
        my_months = [[12, 1, 2], [3, 4, 5], [6, 7, 8]]
        if n in my_months[0]:
            print("Winter")
        elif n in my_months[1]:
            print("Spring")
        elif n in my_months[2]:
            print("Summer")
        else: 
            print("Autumn")
write_season(n)

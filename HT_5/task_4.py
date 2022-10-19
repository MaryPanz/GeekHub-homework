start_num = (input("Start: "))
end_num = (input("End: "))

def prime_list(start_num, end_num):
    try:
        result =  []
        for number in range(int(start_num), int(end_num) + 1):
            if number > 1:
                for i in range (2, number):
                    if (number % i) == 0:
                        break
                else:
                    result.append(number)
        return result

    except ValueError:
        return("Not an integer!")
    
print(prime_list(start_num, end_num))

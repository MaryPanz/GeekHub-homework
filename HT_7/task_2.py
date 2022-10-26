my_list = list(range(1,100))
result = [number for number in my_list if number > 10 if int(str(number)[1:]) + int(str(number)[:1]) == 10]
print(result)

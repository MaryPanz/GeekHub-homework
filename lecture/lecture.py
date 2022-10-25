
my_list = [1,2]
my_list = [item ** 2 for item in my_list if item % 2 == 0]

my_dict = {}
for item in range(10):
    my_dict[item] = item ** 2
    
my_dict = {item: item ** 2 for item in range(10)}
    
print(my_dict)
    
    
my_str_d = {str(k): str(v) for k, v in my_dict.items()}
print(my_str_d)

# can create all but tuple

my_generator = (item ** 2 for item in range(10))

print(my_generator)

for i in my_generator:
    print(i)
  
# can iter only once

next(my_generator)

def leap_year(start, end):
  years = []
  for year in range(start, end+1):
    if year % 4 and year % 100 !=0 or year % 400 == 0:
      years.append(year)
  return years

for year in leap_years(1900, 2000):
  print(year)
  
  
  def leap_year(start, end):
  for year in range(start, end+1):
    if year % 4 and year % 100 !=0 or year % 400 == 0:
      
        yield year

for year in leap_year(1900, 1910):
  print(year)
  
  
  def my_generator():
    print("One")
    yield
    print("two")
    yield
    print("three")
    
    gen = my_generator()
    

""" for i in range(len(my_list)) not OK
    
    for i in my_list:
        my_value = i    OK
    
    for index, value in enumerate(my_list):
        print(f"{index}: {value}")           OK
    
    x == True:
        if x == True:    Not OK
        
        if x:
        if not x:           OK
        
        x = 5
        if 1 < x < 10:     OK
        
        
        return and print
        
        list/set comprehensions 1 2 oneline 3 function 4 func 567 oneline
        
        """
  

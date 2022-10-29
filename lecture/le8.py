file = open("test.txt", "r") #"w", "a" "rt" - text "wb - binary for img"
print(file.read(10)) # 10 Asci symbols only
print(file.read(10)) # will print 10 next symbols
file.seek(0)
file.close() #need to close the file

# better use context mgr
with open("test.txt", encoding= "utf-8") as file:
    content = file.read()
    print(content)
    
#write file
with open("test.txt", "w", encoding= "utf-8") as file:
    file.write("Meow!!!")
    file.write(""\n")
    
    test_list = [str(i) + str(i-1) for i in range(20)]
    file.write(item + "\n")
    content = "\n".join(test_list)
    file.writelines(content)
    
with open("test.txt", encoding= "utf-8") as file:
    for line in file:
        print(line)
# json - almost like dict work same as with dict
import json


with open("test.json") as file:
    content = json.load(file)
    print(contet)
    print(type(content))
    
with open("test.json") as file:
    content = {"bob": "12345", 12345: "mm"}
    json.dump(content, file)
    
#json writes all in str so "123" and 123 is the same for json
    
    
with open("test.json") as file:
    content = {"bob": "12345", 12345: "mm"}
    json_content = json.dumps(content, file)
    print(json_content)
#json writes all in str so "123" and 123 is the same for json
    
#dumps - now obj, raw obj dump in file method
               
               # csv format

import csv

with open("test.csv", newline = "") as file:
    #reader = csv.reader(file)
    #for row in reader:
    #    print(row)
    reader = csv.DictReader(file, fieldnames = ["one", "two", "three"]) #must be same as columns if bigger for these keys the meaning will be None. If the number is less... new dict is created separately??
    for record in reader:
        print(record)
        
with open("test.csv", newline = "") as file:
    writer = csv.writer(file)
    test_data = [{"Some": 1, "Another": 2}]
    writer.writerows(test_data)
               

        #fieldnames obligator
with open("test.csv", newline = "") as file:
    writer = csv.DictWriter(file, fieldnames= ["Some", "Anotehr"])
    test_data = [{"Some": 1, "Another": 2}]
    writer.header()
    writer.writerows(test_data)
    
    
# pickle  - python format, will be coded in str
import pickle

with opent("test.pickle", "wb") as file:
    data = {"Some": 1234}
    pickle.dump(data,file)

  
 with opent("test.pickle", "rb") as file:
    data = pickle.load(file)
    pickle(type(data))
               
               
  # pickle - you can use any type of data

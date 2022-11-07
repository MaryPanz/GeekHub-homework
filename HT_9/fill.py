import sqlite3


connection = sqlite3.connect("a.db")
connection.execute("INSERT INTO bank(ID,NAME,PASSWORD,BALANCE,TOPUP,WITHDRAW) \
VALUES (?,?,?,?,?,?)", (1, 'bob', 1234, 1000,0,0))
connection.execute("INSERT INTO bank(ID,NAME,PASSWORD,BALANCE,TOPUP,WITHDRAW) \
VALUES (?,?,?,?,?,?)", (2, 'lisa', 2345, 2000,0,0))
connection.execute("INSERT INTO bank(ID,NAME,PASSWORD,BALANCE,TOPUP,WITHDRAW) \
VALUES (?,?,?,?,?,?)", (3, 'kate', 3456, 3000,0,0))
connection.execute("INSERT INTO bank(ID,NAME,PASSWORD,BALANCE,TOPUP,WITHDRAW) \
VALUES (?,?,?,?,?,?)", (4, 'admin', 1111, 4000,0,0))


connection.execute("INSERT INTO banknotes(ID,N10,N20,N50,N100,N200,N500,N1000,TOTAL) \
VALUES (?,?,?,?,?,?,?,?,?)", (1, 10, 10, 10,10,10,10,10,16800))
connection.commit()
connection.close()
print("Records added")

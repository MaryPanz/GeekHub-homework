import sqlite3


connection = sqlite3.connect("a.db")
command = ("""CREATE TABLE IF NOT EXISTS bank(
        ID       INT PRIMARY KEY NOT NULL,
        NAME     TEXT NOT NULL,
        PASSWORD INT NOT NULL,
        BALANCE  INT,
        TOPUP    INT,
        WITHDRAW INT
        );""")
connection.execute(command)
command = ("""CREATE TABLE IF NOT EXISTS banknotes(
        ID INT PRIMARY KEY NOT NULL,
        N10   INT NOT NULL,
        N20   INT NOT NULL,
        N50   INT NOT NULL,
        N100  INT NOT NULL,
        N200  INT NOT NULL,
        N500  INT NOT NULL,
        N1000 INT NOT NULL,
        TOTAL INT NOT NULL
        );""")
connection.execute(command)
command = ("""CREATE TABLE IF NOT EXISTS transactions(
        ID INT PRIMARY KEY,
        NAME   TEXT NOT NULL,
        FLAG   TEXT,
        AMOUNT INT NOT NULL,
        TIME   TEXT
        );""")
connection.execute(command)
connection.close()
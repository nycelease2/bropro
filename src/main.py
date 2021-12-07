import sqlite3
import sys

con = sqlite3.connect('DataBase.db')
cur = con.cursor()

print(' [1] add customer')
print(' [2] add stock')
print(' [3] add order')
print(' [4] print orders')

choice = input(': ')

if choice == "1":
    print('Name of customer*')
    name = input(': ')
    print('Email')
    email = input(': ')
    print('Mobile Number*')
    mob_num = input(': ')

    script1 = ("INSERT INTO user(name,email,mobile_number) VALUES('")
    variablescript = (name,"'","'",email,"'","'",mob_num,"'", ');')

    con.execute("INSERT INTO user(name,email,mobile_number) VALUES('Raaghav', 'nycelease@gmail.com', '9909909901')")
    
    con.commit()
    con.close()
    sys.exit()

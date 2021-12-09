import sqlite3
import sys

running = True
conn = sqlite3.connect('DataBase.db')
c = conn.cursor()
while running == True:
    print(' [1] add customer')
    print(' [2] add stock')
    print(' [3] add order')
    print(' [4] print orders')
    print(' [5] exit')

    choice = input(': ')

    if choice == "1":
        print('Name of customer*')
        name = input(': ')
        print('Email')
        email = input(': ')
        print('Mobile Number*')
        mob_num = input(': ')

        if email != None:
            c.execute("INSERT INTO user(name, mobile_number, email) VALUES(?,?,?)",(name,mob_num,email))
    
        conn.commit()

    if choice == 3:
        print('name of person')
        nameOfperson=input(": ")
        
        print('item')
        orderOfperson=input(": ")


    if choice == 5:
        conn.commit()
        conn.close()
        sys.exit

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

# adding customer
    if choice == "1":
        print('Name of customer*')
        name = input(': ')
        print('Email (if none put null)')
        email = input(': ')
        print('Mobile Number*')
        mob_num = input(': ')

        if email != None:
            c.execute("INSERT INTO user(name, mobile_number, email) VALUES(?,?,?)",(name,mob_num,email))
    
        conn.commit()
        print("success!")

# adding stock
    if choice == "2":
        print('Item Name*')
        iName = input(': ')
        print('Amount(without unit)*')
        amount = input(': ')
        print('unit of measurement*')
        unit = input(': ')
        c.execute("INSERT INTO onSale(item, amount, unit) VALUES(?,?,?)", (iName, amount, unit))
        conn.commit

# add order
    if choice == "3":
        print('name of person')
        nameOfperson=input(": ")
        
        print('item')
        orderOfperson=input(": ")

# exit
    if choice == "5":
        conn.commit()
        conn.close()
        running = False
sys.exit

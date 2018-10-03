import sqlite3
import time

with sqlite3.connect("username.db") as db:
    cursor = db.cursor()
def login(Username,Password):
##        Username = input("Enter your username: ")
##        Password = input("Enter your password: ")
        find_user = ("Select * FROM users WHERE Username = ? AND Password = ?")
        cursor.execute(find_user,[(Username),(Password)])
        results = cursor.fetchall()
        
        if results:
            for i in results:
                print("WELCOME "+i[0]+"!")
            return 1               
        else:
            print("Invalid Username or Password.")
            return 0



import sys
from http.client import responses

from DBhelper import DBhelper
class FlipKart:
    def __init__(self):
        #connect to the database
        self.db = DBhelper()
        self.menu()
    
    def menu(self):

        user_input = input(
            "1.Enter 1 to register\n"
            "2.Enter 2 to login\n"
            "3.Anything else to leave\n"
            )


        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name = input("enter ur name")
        email = input("enter ur email")
        password = input("Enter ur password")

        response = self.db.register(name,email,password)

        if response:
            print("registration successfull")
            self.menu()
        else:
            print("registration failed")
            self.menu()
obj = FlipKart()


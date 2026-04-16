class User:
    def welcome(self):
        print("Welcome, user!")

class Admin(User):
    def welcome(self):
        print("Welcome, admin! You have full access.")

class Guest(User):
    def welcome(self):
        print("Welcome, guest! Your access is limited.")

admin = Admin()
admin.welcome()

guest = Guest()
guest.welcome()

"""
Welcome, admin! You have full access.
Welcome, guest! Your access is limited.
"""
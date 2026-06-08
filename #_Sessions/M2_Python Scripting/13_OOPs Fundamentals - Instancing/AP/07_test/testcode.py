# bank system 

#  TAsk1 : classs Bank System 
# 
#   Initializing object it takes two values holder_name , Balance  

# class attribute bank_name, total_number_of_acc  
class BankAccount:

    bank_name = "Reserve Bank"
    total_number_of_acc = 0

    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

        BankAccount.total_number_of_acc += 1

        # print(f"Account Holder:{self.holder_name}" )
        # print(f"Balance: {self.balance}")

    def show_balance(self):
        print(f"Bank Name: {self.bank_name}")
        print(f"Name: {self.holder_name}")
        print(f"Balance: {self.balance}")

    def withdraw(self, amount_withdraw):
        if amount_withdraw > self.balance:
            print("Insufficient Balance in account. ")

        else:
            self.balance = self.balance - amount_withdraw
            print(f"{amount_withdraw} Withdraw successful! .")
            print(f"New Balance: {self.balance}")

    def deposit(self, amount_deposit):
        if amount_deposit < 0:
            print("Deposit Amount cannot be negative in value. ")

        else:
            self.balance = self.balance + amount_deposit
            print(f"{amount_deposit} deposit is successful!")
            print(f"New Balance :{self.balance}")

    @staticmethod
    def policy():
        print("Account Balance should not be less than 2000!. If Less charges Apply.")

    @staticmethod #static method to access account1 and and not give out any error 
    def bank_details():
        print(f"Bank name: {BankAccount.bank_name} , Total Number of Acoounts: {BankAccount.total_number_of_acc}")


account1 = BankAccount("Raj", 12000)
account1.show_balance()
account1.withdraw(2000)
account1.deposit(200)
account1.policy()
account1.bank_details()
# BankAccount.policy()
# BankAccount.bank_details()

# account2 = BankAccount("Raja", 21000)
# account3 = BankAccount("Rajesh", 2100)
# BankAccount.bank_details()

# BankAccount.bank_name = "Indian Bank" # class attribute method 
# # account3.update_bank("Indian Bank")
# account3.show_balance()

# BankAccount.bank_details()
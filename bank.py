from random import choices
import string


class Bank:
    def __init__(self, __accounts):
        self.__accounts = {}

    def generate_id():
        return ''.join(choices(string.ascii_letters, k=5) + choices(string.punctuation, k=10))

    def create_account(self, __acc_id, __initial_balance=0):
        if __acc_id in self.__accounts:
            print("The account was already registered")
        else:
            self.__accounts[__acc_id] = __initial_balance
    
    def deposit(self, __acc_id, __value):
        if __acc_id in self.__accounts:
            self.__accounts[__acc_id] += __value
            print(f"Deposit of {__value} made successfully to {__acc_id}")
    
    def withdraw(self, __acc_id, __value):
        if __acc_id in self.__accounts:
            if self.__accounts[__acc_id] >= __value:
                self.__accounts[__acc_id] -= __value
                print(f"the withdraw of {__value} made sucessfully")
                print(f"Current balance: {self.__accounts[__acc_id]}")
            else:
                print("Insufficient funds")

__acc1_id = Bank.generate_id()

account1 = Bank(__acc1_id)
print("\n")
account1.create_account(__acc1_id)
account1.deposit(__acc1_id, 19200)
account1.withdraw(__acc1_id, 10366)
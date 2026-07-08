import secrets


class Account:

    def __init__(self):
        self.full_name = ""
        self.account_number = self.generate_account_number()
        self.bvn = ""
        self.pin = ""
        self.balance = 0.0
        self.active = False

    def generate_account_number(self):
        account_number = ""

        for count in range(10):
            account_number += str(secrets.randbelow(10))

        return account_number

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_bvn(self, bvn):
        self.bvn = bvn

    def set_pin(self, pin):
        self.pin = pin

    def get_full_name(self):
        return self.full_name

    def get_account_number(self):
        return self.account_number

    def get_pin(self):
        return self.pin

    def get_bvn(self):
        return self.bvn

    def get_balance(self):
        return self.balance

    def get_active(self):
        if self.active:
            return "Active"
        else:
            return "Not Active"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.active = True

    def transfer(self, receiver, amount):

        if not self.active:
           print("Account has been deactivated")
           return

        if not receiver.active:
           print("receiver account has been deactivated")
           return

        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            receiver.deposit(amount)

            print("\nTransfer successful")
            print("Balance:", self.balance)
        else:
            print("Insufficient Balance.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

            print("\nWithdrawal Successful")
            print("Your Current Balance is:", self.balance)
        else:
            print("Insufficient Balance.")

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("\nPIN changed successfully!")

    def deactivate(self):
        self.active = False
        print("Account deactivated successfully.")

    def verify_pin(self, pin):
        return self.pin == pin

    def verify_account_number(self, account_number):
        return self.account_number == account_number

    def validate_bvn(self, bvn):
        return len(bvn) == 11

    def validate_pin(self, pin):
        return len(pin) == 4

    def validate_account_number(self, account_number):
        return len(account_number) == 10

    def validate_amount(self, amount):
        return amount > 0
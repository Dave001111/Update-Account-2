import secrets


class Account:

    def __init__(self):
        self.fullName = ""
        self.accountNumber = self.generateAccountNumber()
        self.bvn = ""
        self.pin = ""
        self.balance = 0.0
        self.active = False

    def generateAccountNumber(self):
        accountNumber = ""

        for count in range(10):
            accountNumber += str(secrets.randbelow(10))

        return accountNumber

    def setFullName(self, fullName):
        self.fullName = fullName

    def setBvn(self, bvn):
        self.bvn = bvn

    def setPin(self, pin):
        self.pin = pin

    def getFullName(self):
        return self.fullName

    def getAccountNumber(self):
        return self.accountNumber

    def getPin(self):
        return self.pin

    def getBvn(self):
        return self.bvn

    def getBalance(self):
        return self.balance

    def getActive(self):
        if self.active:
            return "Active"
        else:
            return "Not Active"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.active = True

    def transfer(self, receiver, amount):
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

    def changePin(self, newPin):
        self.pin = newPin
        print("\nPIN changed successfully!")

    def deactivate(self):
        self.active = False
        print("Account deactivated successfully.")

    def verifyPin(self, pin):
        return self.pin == pin

    def verifyAccountNumber(self, accountNumber):
        return self.accountNumber == accountNumber

    def validateBvn(self, bvn):
        return len(bvn) == 11

    def validatePin(self, pin):
        return len(pin) == 4

    def validateAccountNumber(self, accountNumber):
        return len(accountNumber) == 10

    def validateAmount(self, amount):
        return amount > 0
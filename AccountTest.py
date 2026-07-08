def errorPinMessage():
    print("Invalid PIN. PIN must be exactly 4 digits.")
    print("Re enter your PIN: ", end="")


def errorAccountNumberMessage():
    print("Invalid Account Number. Account Number must be exactly 10 digits.")
    print("Re enter your Account Number: ", end="")


def accountMissingMessage():
    print("Account number not found.")
    print("Re enter your Account Number: ", end="")


def incorrectPinMessage():
    print("Incorrect PIN.")
    print("Enter your PIN again: ", end="")


def errorAmountMessage():
    print("Amount must be higher than 0.")
    print("Enter amount again: ", end="")


options = [
    "Create Account",
    "Deposit",
    "Transfer",
    "Withdrawal",
    "Change Pin",
    "Check balance",
    "Deactivation"
]

accounts = []

print("Welcome To David Bank")
print("================================")

answer = "yes"

while answer.lower() == "yes":

    count = 1

    for index in range(len(options)):
        print(f"{count}. {options[index]}")
        count += 1

    choice = int(input("\nSelect an option: "))

    account = Account()
    amount = 0
    account_found = False

if choice == 1:

    account = Account()

    print("\n========== Create Your Account ============")
    print("------------------------------------------")

    fullName = input("Enter Your Full Name: ")
    account.setFullName(fullName)

    bvn = input("Enter Your BVN: ")

    while not account.validateBvn(bvn):
        print("Invalid BVN. BVN must not be less or higher than 11 digits.")
        bvn = input("Re Enter Your BVN: ")

    bvnExists = True

    while bvnExists:

        bvnExists = False

        for index in range(len(accounts)):

            if accounts[index].getBvn() == bvn:

                print("BVN already exists.")
                bvn = input("Enter another BVN: ")

                bvnExists = True
                break

    account.setBvn(bvn)

    pin = input("Set-up a 4-digit PIN: ")

    while not account.validatePin(pin):
        errorPinMessage()
        pin = input()

    account.setPin(pin)

    print("\nAccount Created Successfully")
    print("================================")
    print("Full Name      :", account.getFullName())
    print("Account Number :", account.getAccountNumber())
    print("BVN            :", account.getBvn())
    print("PIN            :", account.getPin())
    print("Balance        :", account.getBalance())
    print("Status         :", account.getActive())

    accounts.append(account)


elif choice == 2:

    print("========== Deposit Money ==========")
    print("--------------------------------------")

    accountNumber = input("Enter your Account Number: ")

    while not account.validateAccountNumber(accountNumber):
        errorAccountNumberMessage()
        accountNumber = input()

    accountFound = False

    for index in range(len(accounts)):

        account = accounts[index]

        if account.verifyAccountNumber(accountNumber):

            pin = input("Enter your PIN: ")

            while not account.validatePin(pin):
                errorPinMessage()
                pin = input()

            while not account.verifyPin(pin):
                incorrectPinMessage()
                pin = input()

            amount = float(input("Enter amount: "))

            while not account.validateAmount(amount):
                errorAmountMessage()
                amount = float(input())

            accountFound = True

            account.deposit(amount)

            print("\nMoney Deposited Successfully")
            print("================================")
            print("Full Name :", account.getFullName())
            print("Balance   :", account.getBalance())
            print("Status    :", account.getActive())

            break

    if not accountFound:
        print("Account number not found.")


elif choice == 3:

    print("========== Transfer ==========")
    print("---------------------------------")

    accountNumber = input("Enter your Account Number: ")

    while len(accountNumber) != 10:
        errorAccountNumberMessage()
        accountNumber = input()

    senderFound = False

    for index in range(len(accounts)):

        sender = accounts[index]

        if sender.verifyAccountNumber(accountNumber):

            senderFound = True

            pin = input("Enter your PIN: ")

            while not sender.validatePin(pin):
                errorPinMessage()
                pin = input()

            while not sender.verifyPin(pin):
                incorrectPinMessage()
                pin = input()

            receiverAccount = input("Enter The Receiver's Account Number: ")

            while len(receiverAccount) != 10:
                errorAccountNumberMessage()
                receiverAccount = input()

            if sender.verifyAccountNumber(receiver_account):
                print("You cannot transfer money to the same account.")
                break

            receiverFound = False

            for count in range(len(accounts)):

                receiver = accounts[count]

                if receiver.verifyAccountNumber(receiverAccount):

                    receiver_found = True

                    amount = float(input("Enter amount: "))

                    while not sender.validateAmount(amount):
                        errorAmountMessage()
                        amount = float(input())

                    sender.transfer(receiver, amount)

                    print("================================")
                    print("Sender Balance   :", sender.getBalance())
                    print("Receiver Balance :", receiver.getBalance())

                    break

            if not receiverFound:
                print("Receiver account number not found.")

    if not senderFound:
        print("Account number not found.")


elif choice == 4:

    print("========== Withdrawal ==========")
    print("---------------------------------")

    accountNumber = input("Enter your Account Number: ")

    while len(accountNumber) != 10:
        errorAccountNumberMessage()
        accountNumber = input()

    accountFound = False

    for index in range(len(accounts)):

        account = accounts[index]

        if account.verifyAccountNumber(account_number):

            accountFound = True

            pin = input("Enter your PIN: ")

            while not account.validatePin(pin):
                errorPinMessage()
                pin = input()

            while not account.verifyPin(pin):
                incorrectPinMessage()
                pin = input()

            amount = float(input("Enter amount: "))

            while not account.validateAmount(amount):
                errorAmountMessage()
                amount = float(input())

            account.withdraw(amount)

            print("================================")
            print("Full Name :", account.getFullName())
            print("Balance   :", account.getBalance())

            break

    if not accountFound:
        print("Account number not found.")


elif choice == 5:

    print("========== Change Pin ==========")
    print("---------------------------------")

    accountNumber = input("Enter your Account Number: ")

    while len(accountNumber) != 10:
        errorAccountNumberMessage()
        accountNumber = input()

    accountFound = False

    for index in range(len(accounts)):

        account = accounts[index]

        if account.verifyAccountNumber(accountNumber):

            accountFound = True

            pin = input("Enter your PIN: ")

            while not account.validatePin(pin):
                errorPinMessage()
                pin = input()

            while not account.verifyPin(pin):
                incorrectPinMessage()
                pin = input()

            newPin = input("Enter Your New PIN: ")

            while not account.validatePin(new_pin):
                errorPinMessage()
                newPin = input()

            account.changePin(new_pin)
    if not accountFound:
        print("Account number not found.")


elif choice == 6:

    print("========== Check Balance ==========")
    print("-----------------------------------")

    accountNumber = input("Enter your Account Number: ")

    while len(accountNumber) != 10:
        errorAccountNumberMessage()
        accountNumber = input()

    accountFound = False

    for index in range(len(accounts)):

        account = accounts[index]

        if account.verifyAccountNumber(accountNumber):

            accountFound = True

            pin = input("Enter your PIN: ")

            while not account.validatePin(pin):
                errorPinMessage()
                pin = input()

            while not account.verifyPin(pin):
                incorrectPinMessage()
                pin = input()

            print("\n========== Account Details ==========")
            print("Full Name      :", account.getFullName())
            print("Account Number :", account.getAccountNumber())
            print("Balance        :", account.getBalance())
            print("Status         :", account.getActive())

            break

    if not accountFound:
        print("Account number not found.")


elif choice == 7:

    print("========== Deactivate Account ==========")
    print("-----------------------------------------")

    account_number = input("Enter your Account Number: ")

    while len(account_number) != 10:
        errorAccountNumberMessage()
        accountNumber = input()

    accountFound = False

    for index in range(len(accounts)):

        account = accounts[index]

        if account.verifyAccountNumber(accountNumber):

            accountFound = True

            pin = input("Enter your PIN: ")

            while not account.validatePin(pin):
                errorPinMessage()
                pin = input()

            while not account.verifyPin(pin):
                incorrectPinMessage()
                pin = input()

            deactivate = input("Do you want to deactivate your account? (yes/no): ")

            if deactivate.lower() == "yes":
                account.deactivate()
            else:
                print("Account deactivation cancelled.")

            break

    if not accountFound:
        print("Account number not found.")

    answer = input("\nDo you want to continue? (yes/no): ")

    if answer.lower() == "no":
        print("\nThanks for banking with us.")
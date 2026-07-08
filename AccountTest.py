from Account import Account
def error_pin_message():
    print("Invalid PIN. PIN must be exactly 4 digits.")
    print("Re enter your PIN: ", end="")


def error_account_number_message():
    print("Invalid Account Number. Account Number must be exactly 10 digits.")
    print("Re enter your Account Number: ", end="")


def account_missing_message():
    print("Account number not found.")
    print("Re enter your Account Number: ", end="")


def incorrect_pin_message():
    print("Incorrect PIN.")
    print("Enter your PIN again: ", end="")


def error_amount_message():
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

   
   amount = 0
   account_found = False

   if choice == 1:

     account = Account()

     print("\n========== Create Your Account ============")
     print("------------------------------------------")

     full_name = input("Enter Your Full Name: ")
     account.set_full_name(full_name)

     bvn = input("Enter Your BVN: ")

     while not account.validate_bvn(bvn):
        print("Invalid BVN. BVN must not be less or higher than 11 digits.")
        bvn = input("Re Enter Your BVN: ")

     bvn_exists = True

     while bvn_exists:

        bvn_exists = False

        for index in range(len(accounts)):

            if accounts[index].get_bvn() == bvn:

                print("BVN already exists.")
                bvn = input("Enter another BVN: ")

                bvn_exists = True
                break

     account.set_bvn(bvn)

     pin = input("Set-up a 4-digit PIN: ")

     while not account.validate_pin(pin):
        error_pin_message()
        pin = input()

     account.set_pin(pin)

     print("\nAccount Created Successfully")
     print("================================")
     print("Full Name      :", account.get_full_name())
     print("Account Number :", account.get_account_number())
     print("BVN            :", account.get_bvn())
     print("PIN            :", account.get_pin())
     print("Balance        :", account.get_balance())
     print("Status         :", account.get_active())

     accounts.append(account)


   elif choice == 2:

     print("========== Deposit Money ==========")
     print("--------------------------------------")

     account_number = input("Enter your Account Number: ")

     while not account.validate_account_number(account_number):
        error_account_number_message()
        account_number = input()

     account_found = False

     for index in range(len(accounts)):

        account = accounts[index]

        if account.verify_account_number(account_number):

            pin = input("Enter your PIN: ")

            while not account.validate_pin(pin):
                error_pin_message()
                pin = input()

            while not account.verify_pin(pin):
                incorrect_pin_message()
                pin = input()

            amount = float(input("Enter amount: "))

            while not account.validate_amount(amount):
                error_amount_message()
                amount = float(input())

            account_found = True

            account.deposit(amount)

            print("\nMoney Deposited Successfully")
            print("================================")
            print("Full Name :", account.get_full_name())
            print("Balance   :", account.get_balance())
            print("Status    :", account.get_active())

            break

     if not account_found:
        print("Account number not found.")


   elif choice == 3:

     print("========== Transfer ==========")
     print("---------------------------------")

     account_number = input("Enter your Account Number: ")

     while len(account_number) != 10:
        error_account_number_message()
        account_number = input()

     sender_found = False

     for index in range(len(accounts)):

        sender = accounts[index]

        if sender.verify_account_number(account_number):

            sender_found = True

            pin = input("Enter your PIN: ")

            while not sender.validate_pin(pin):
                error_pin_message()
                pin = input()

            while not sender.verify_pin(pin):
                incorrect_pin_message()
                pin = input()

            receiver_account = input("Enter The Receiver's Account Number: ")

            while len(receiver_account) != 10:
                error_account_number_message()
                receiver_account = input()

            if sender.verify_account_number(receiver_account):
                print("You cannot transfer money to the same account.")
                break

            receiver_found = False

            for count in range(len(accounts)):

                receiver = accounts[count]

                if receiver.verify_account_number(receiver_account):

                    receiver_found = True

                    amount = float(input("Enter amount: "))

                    while not sender.validate_amount(amount):
                        error_amount_message()
                        amount = float(input())

                    sender.transfer(receiver, amount)

                    

                    break

            if not receiver_found:
                print("Receiver account number not found.")

     if not sender_found:
        print("Account number not found.")


   elif choice == 4:

     print("========== Withdrawal ==========")
     print("---------------------------------")

     account_number = input("Enter your Account Number: ")

     while len(account_number) != 10:
        error_account_number_message()
        account_number = input()

     account_found = False

     for index in range(len(accounts)):

        account = accounts[index]

        if account.verify_account_number(account_number):

            account_found = True

            pin = input("Enter your PIN: ")

            while not account.validate_pin(pin):
                error_pin_message()
                pin = input()

            while not account.verify_pin(pin):
                incorrect_pin_message()
                pin = input()

            amount = float(input("Enter amount: "))

            while not account.validate_amount(amount):
                error_amount_message()
                amount = float(input())

            account.withdraw(amount)

            print("================================")
            print("Full Name :", account.get_full_name())
            print("Balance   :", account.get_balance())

            break

     if not account_found:
        print("Account number not found.")


   elif choice == 5:

     print("========== Change Pin ==========")
     print("---------------------------------")

     account_number = input("Enter your Account Number: ")

     while len(account_number) != 10:
        error_account_number_message()
        account_number = input()

     account_found = False

     for index in range(len(accounts)):

        account = accounts[index]

        if account.verify_account_number(account_number):

            account_found = True

            pin = input("Enter your PIN: ")

            while not account.validate_pin(pin):
                error_pin_message()
                pin = input()

            while not account.verify_pin(pin):
                incorrect_pin_message()
                pin = input()

            new_pin = input("Enter Your New PIN: ")

            while not account.validate_pin(new_pin):
                error_pin_message()
                new_pin = input()

            account.change_pin(new_pin)
     if not account_found:
        print("Account number not found.")


   elif choice == 6:

     print("========== Check Balance ==========")
     print("-----------------------------------")

     account_number = input("Enter your Account Number: ")

     while len(account_number) != 10:
        error_account_number_message()
        account_number = input()

     account_found = False

     for index in range(len(accounts)):

        account = accounts[index]

        if account.verify_account_number(account_number):

            account_found = True

            pin = input("Enter your PIN: ")

            while not account.validate_pin(pin):
                error_pin_message()
                pin = input()

            while not account.verify_pin(pin):
                incorrect_pin_message()
                pin = input()

            print("\n========== Account Details ==========")
            print("Full Name      :", account.get_full_name())
            print("Account Number :", account.get_account_number())
            print("Balance        :", account.get_balance())
            print("Status         :", account.get_active())

            break

     if not account_found:
        print("Account number not found.")


   elif choice == 7:

     print("========== Deactivate Account ==========")
     print("-----------------------------------------")

     account_number = input("Enter your Account Number: ")

     while len(account_number) != 10:
        error_account_number_message()
        account_number = input()

     account_found = False

     for index in range(len(accounts)):

        account = accounts[index]

        if account.verify_account_number(account_number):

            account_found = True

            pin = input("Enter your PIN: ")

            while not account.validate_pin(pin):
                error_pin_message()
                pin = input()

            while not account.verify_pin(pin):
                incorrect_pin_message()
                pin = input()

            deactivate = input("Do you want to deactivate your account? (yes/no): ")

            if deactivate.lower() == "yes":
                account.deactivate()
            else:
                print("Account deactivation cancelled.")

            break

     if not account_found:
        print("Account number not found.")

   answer = input("\nDo you want to continue? (yes/no): ")

   if answer.lower() == "no":
      print("\nThanks for banking with us.")
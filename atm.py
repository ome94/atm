users = {}

import random
from datetime import datetime

def init():
    print("Welcome to ZuriBank")

    has_account = None

    while has_account is None or has_account not in [1, 2]:
        try:
            has_account = int(input("""
            Do you have account with us: 
            [1] Yes [2] No
            """))

            if has_account not in [1, 2]:
                print("ERROR!\nInvalid option selected, select 1 or 2")

        except ValueError:
            print("ERROR!\nInvalid input, only numeric inputs are allowed")

    if has_account == 1:
        login()

    elif has_account == 2:
        register()

def register():
    print("****** Account Registration *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    acc_no = generate_acc_no()

    users[acc_no] = [first_name, last_name, email, password]

    print(" == ==== ====== ===== ===")
    print("Your Account Has been created")
    print("""
    Your account details are as follows:
        First Name: %s
        Last Name: %s
        Email: %s
        Account Number: %d
        """ % first_name, last_name, email, acc_no)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()
 
def login():
    print("********* Login ***********")

    acc_no_input = None

    while acc_no_input is None or acc_no_input not in users:
        print("ERROR!\nInvalid account number! Try again")

        acc_no_input = input("What is your account number?\n")

    password = None

    while password is None or password != users[acc_no_input[3]]:
        password = input("Please type your password\n")

        if password != users[acc_no_input[3]]:
            print("ERROR!\nWrong password! Please enter a correct password.")

    bank_operation(users[acc_no_input])

def generate_acc_no():
    return random.randrange(1111111111, 9999999999)

def bank_operation(user):
    now = datetime.now()
    name = user[0] + user[1]
    balance = user[4]

    print("Welcome %s" % name)
    print("Date: %s" % now.strftime("%d-%m-%Y"))
    print("Time: %s" % now.strftime("%H:%M:%S"))
    
    selected_option = None
    while selected_option is None or selected_option not in [1, 2, 3]:
        try:
            selected_option = int(input("""
            Please select an option:

            These are the available options:
            [1]. Withdrawal
            [2]. Cash Deposit
            [3]. Complaint
            """))
            
            if selected_option not in [1, 2, 3]:
                print("ERROR!\nWrong option selected")

        except ValueError:
            print("ERROR!\nWrong input entered! Please try again")
    
    if (selected_option == 1):
        print("You selected %s (Withdraw)" % selected_option)
        if balance is None:
            choice = None
            while choice is None or choice not in [1, 2]:
                try:
                    choice = int(input("""
                    You have not made a deposit yet, would you like to make a deposit
                    [1] Yes [2] No
                    """))

        withdrawal =  None
        while withdrawal is None:
            try:
                withdrawal = int(input("How much would you like to withdraw?\n"))
            except ValueError:
                print("ERROR! Invalid input\n Input a numeric amount")
        
        if balance > withdrawal:
            balance -= withdrawal
            print("Take your cash")
        
        else:
            print("ERROR: Insufficient funds")
        
    elif (selected_option == 2):
        print("You selected %s (Deposit)" % selected_option)
        deposit = int(input("How much would you like to deposit?\n"))
        usersBalances[userId] += deposit
        print("Current Balance: %s" % usersBalances[userId])
        
    elif (selected_option == 3):
        print("You selected %s (Complaint)" % selected_option)
        complaint = input("What issue would you like to report?\n")
        print("Thank you for contacting us")
        
    else:
        print("Invalid option selected, please try again")

name = input("What is your username? \n")
allowedUsers = ["Seyi", "Mike", "Love"]
allowedPasswords = ["passwordSeyi", "passwordMike", "passwordLove"]
usersBalances = [10000, 50000, 20000]

if (name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if (password == allowedPasswords[userId]):
        
        print("Welcome %s" % name)
        print("Date: 02-04-2021")
        print("Time: 09:30AM\n\n")
        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")
        
        selectedOption = int(input("Please select an option:\n"))
        
        if (selectedOption == 1):
            print("You selected %s (Withdraw)" % selectedOption)
            withdrawal = int(input("How much would you like to withdraw?\n"))
            
            if (usersBalances[userId] > withdrawal):
                usersBalances[userId] -= withdrawal
                print("Take your cash")
            
            else:
                print("Error: Insufficient funds")
            
        elif (selectedOption == 2):
            print("You selected %s (Deposit)" % selectedOption)
            deposit = int(input("How much would you like to deposit?\n"))
            usersBalances[userId] += deposit
            print("Current Balance: %s" % usersBalances[userId])
            
        elif (selectedOption == 3):
            print("You selected %s (Complaint)" % selectedOption)
            complaint = input("What issue would you like to report?\n")
            print("Thank you for contacting us")
            
        else:
            print("Invalid option selected, please try again")
        
    else:
        print("Password incorrect, please try again")

else:
    print("Name not found, please try again")

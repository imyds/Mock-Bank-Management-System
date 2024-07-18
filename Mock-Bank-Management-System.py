import pickle
import os
import pathlib
import sqlite3
import datetime as dt

conn = sqlite3.connect('bank.db')
cur = conn.cursor()

# Create tables if not exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS customer_details2015(
        acct_no INTEGER PRIMARY KEY,
        acct_name VARCHAR(25),
        phone_no BIGINT CHECK(length(phone_no) >= 11),
        address VARCHAR(25),
        cr_amt FLOAT
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS customer_details2016(
        username VARCHAR(25) PRIMARY KEY,
        passwrd VARCHAR(25) NOT NULL
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS transactions(
        acct_no INTEGER,
        date DATE,
        withdrawal_amt BIGINT,
        amount_added BIGINT
    )
''')

# Account class definition
class Account:
    def __init__(self):
        self.accNo = 0
        self.name = ''
        self.deposit = 0
        self.type = ''

    def createAccount(self):
        self.accNo = int(input("Enter the account number: "))
        self.name = input("Enter the account holder name: ")
        self.type = input("Enter the type of account [C/S]: ")
        self.deposit = int(input("Enter the initial amount (>=500 for Savings and >=1000 for Current): "))
        print("\nAccount Created Successfully!")

    def showAccount(self):
        print("\nAccount Number:", self.accNo)
        print("Account Holder Name:", self.name)
        print("Type of Account:", self.type)
        print("Balance:", self.deposit)

    def modifyAccount(self):
        print("\nAccount Number:", self.accNo)
        self.name = input("Modify Account Holder Name: ")
        self.type = input("Modify Type of Account: ")
        self.deposit = int(input("Modify Balance: "))

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        if self.deposit >= amount:
            self.deposit -= amount
        else:
            print("Insufficient balance!")

    def report(self):
        print(self.accNo, " ", self.name, " ", self.type, " ", self.deposit)

    def getAccountNo(self):
        return self.accNo

    def getAcccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit

# Function to write account details to file using pickle
def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else:
        oldlist = [account]

    with open('accounts.data', 'wb') as outfile:
        pickle.dump(oldlist, outfile)

# Function to display all accounts from file
def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            mylist = pickle.load(infile)
            for item in mylist:
                print("Account Number:", item.accNo)
                print("Account Holder Name:", item.name)
                print("Type of Account:", item.type)
                print("Balance:", item.deposit)
    else:
        print("No records to display")

# Function to display specific account details from file
def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            mylist = pickle.load(infile)
            found = False
            for item in mylist:
                if item.accNo == num:
                    print("\nYour account Balance is:", item.deposit)
                    found = True
                    break
            if not found:
                print("No existing record with this number")
    else:
        print("No records to search")

# Function to deposit or withdraw from a specific account
def depositAndWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            mylist = pickle.load(infile)
            for item in mylist:
                if item.accNo == num1:
                    if num2 == 1:
                        amount = int(input("Enter the amount to deposit: "))
                        item.deposit += amount
                        print("Your account is updated")
                    elif num2 == 2:
                        amount = int(input("Enter the amount to withdraw: "))
                        if item.deposit >= amount:
                            item.deposit -= amount
                            print("Your account is updated")
                        else:
                            print("Insufficient balance!")

            with open('newaccounts.data', 'wb') as outfile:
                pickle.dump(mylist, outfile)
            os.remove('accounts.data')
            os.rename('newaccounts.data', 'accounts.data')
    else:
        print("No records to search")

# Function to delete an account
def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            oldlist = pickle.load(infile)
            newlist = [item for item in oldlist if item.accNo != num]
            with open('newaccounts.data', 'wb') as outfile:
                pickle.dump(newlist, outfile)
            os.remove('accounts.data')
            os.rename('newaccounts.data', 'accounts.data')
            print("Account deleted successfully")
    else:
        print("No records to delete")

# Function to modify an account
def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        with open('accounts.data', 'rb') as infile:
            oldlist = pickle.load(infile)
            for item in oldlist:
                if item.accNo == num:
                    item.name = input("Enter the account holder name: ")
                    item.type = input("Enter the account type: ")
                    item.deposit = int(input("Enter the amount: "))
            with open('newaccounts.data', 'wb') as outfile:
                pickle.dump(oldlist, outfile)
            os.remove('accounts.data')
            os.rename('newaccounts.data', 'accounts.data')
            print("Account modified successfully")
    else:
        print("No records to modify")

# Main menu loop
while True:
    print("\n=========================")
    print("WELCOME TO YDS BANK")
    print(dt.datetime.now())
    print("=========================")
    print("1. Create Bank Account")
    print("2. Transaction")
    print("3. Customer Details")
    print("4. Transaction Details")
    print("5. Delete Account")
    print("6. New Account")
    print("7. Deposit Amount")
    print("8. Withdraw Amount")
    print("9. Balance Enquiry")
    print("10. All Account Holder List")
    print("11. Close an Account")
    print("12. Modify an Account")
    print("13. Quit")
    print("=========================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        acc = Account()
        acc.createAccount()
        writeAccountsFile(acc)

    elif choice == 2:
        num = int(input("Enter Account Number: "))
        depositAndWithdraw(num, 2)

    elif choice == 3:
        num = int(input("Enter Account Number: "))
        displaySp(num)

    elif choice == 4:
        num = int(input("Enter Account Number: "))
        displaySp(num)

    elif choice == 5:
        num = int(input("Enter Account Number: "))
        deleteAccount(num)

    elif choice == 6:
        acc = Account()
        acc.createAccount()
        writeAccountsFile(acc)

    elif choice == 7:
        num = int(input("Enter Account Number: "))
        depositAndWithdraw(num, 1)

    elif choice == 8:
        num = int(input("Enter Account Number: "))
        depositAndWithdraw(num, 2)

    elif choice == 9:
        num = int(input("Enter Account Number: "))
        displaySp(num)

    elif choice == 10:
        displayAll()

    elif choice == 11:
        num = int(input("Enter Account Number: "))
        deleteAccount(num)

    elif choice == 12:
        num = int(input("Enter Account Number: "))
        modifyAccount(num)

    elif choice == 13:
        print("Thank you for visiting YDS Bank!")
        break

    else:
        print("Invalid choice. Please try again.")

# Close database connection
conn.close()

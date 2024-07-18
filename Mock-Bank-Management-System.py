
import pickle
import os
import pathlib
import sqlite3
conn=sqlite3.connect('bank.db')
cur = conn.cursor()
cur.execute('create table customer_details2015(acct_no int primary     key,acct_name varchar(25) ,phone_no bigint(25) check(phone_no>11),address varchar(25),cr_amt float )')
cur.execute('create table customer_details2016(username varchar(25) primary key,passwrd varchar(25) not null )')
cur.execute('create table transactions(acct_no int(11),date date ,withdrawal_amt bigint(20),amount_added bigint(20) )')
cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')
print('======================================================WELCOME TO YDS BANK============================================================')
import datetime as dt
print(dt.datetime.now())
print('1.REGISTER')
print()
print('2.LOGIN')
print()



n=int(input('enter your choice='))
print()

if n== 1:
     name=input('Enter a Username=')
     print()
     passwd=int(input('Enter a 4 DIGIT Password='))
     print()
     V_SQLInsert="INSERT  INTO customer_details2016 (passwrd,username) values (" +  str (passwd) + ",' " + name + " ') "
     cur.execute(V_SQLInsert)
     conn.commit()
     print()
     print('USER created succesfully')


if  n==2 :
     name=input('Enter your Username=')
     print()
     passwd=int(input('Enter your 4 DIGIT Password='))
     V_Sql_Sel="select * from customer_details2016 where passwrd='"+str (passwd)+"' and username=  ' " +name+ " ' "
     cur.execute(V_Sql_Sel)
     if cur.fetchone() is  None:
          print()
          print('Invalid username or password')
     else:
          print()
          import menu
class Account :
    accNo = 0
    name = ''
    deposit=0
    type = ''

    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
        print("\n\n\nAccount Created")

    def showAccount(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)

    def modifyAccount(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))

    def depositAmount(self,amount):
        self.deposit += amount

    def withdrawAmount(self,amount):
        self.deposit -= amount

    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)

    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit







def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else :
        print("No records to display")


def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print("Your account Balance is = ",item.deposit)
                found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")

def depositAndWithdraw(num1,num2):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updted")
                elif num2 == 2 :
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("You cannot withdraw larger amount")

    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')

def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account Type : ")
                item.deposit = int(input("Enter the Amount : "))

        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def writeAccountsFile(account) :

    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')




c = 'y'
while c == 'y':

                         print()
                         print('1.CREATE BANK ACCOUNT')
                         print()
                         print('2.TRANSACTION')
                         print()
                         print('3.CUSTOMER DETAILS')
                         print()
                         print('4.TRANSACTION DETAILS')
                         print()
                         print('5.DELETE ACCOUNT')
                         print()

                         print("6. NEW ACCOUNT")
                         print()
                         print("7. DEPOSIT AMOUNT")
                         print()
                         print("8. WITHDRAW AMOUNT")
                         print()
                         print("9. BALANCE ENQUIRY")
                         print()
                         print("10. ALL ACCOUNT HOLDER LIST")
                         print()
                         print("11. CLOSE AN ACCOUNT")
                         print()
                         print("12. MODIFY AN ACCOUNT")
                         print()
                         print('13.QUIT')
                         print()

                         print("\tSelect Your Option (1-13) ")

                         n=int(input('Enter your CHOICE='))
                         print()

                         if n == 1:

                                    acc_no=int(input('Enter your ACCOUNT NUMBER='))
                                    print()
                                    acc_name=input('Enter your ACCOUNT NAME=')
                                    print()
                                    ph_no=int(input('Enter your PHONE NUMBER='))
                                    print()
                                    add=(input('Enter your place='))
                                    print()
                                    cr_amt=int(input('Enter your credit amount='))
                                    V_SQLInsert="INSERT  INTO customer_details2015 values (" +  str (acc_no) + ",' " + acc_name + " ',"+str(ph_no) + ",' " +add + " ',"+ str (cr_amt) + " ) "
                                    cur.execute(V_SQLInsert)
                                    print()
                                    print('Account Created Succesfully!!!!!')
                                    conn.commit()


                         if n == 2:
                              acct_no=int(input('Enter Your Account Number='))
                              cur.execute('select * from customer_details2015 where acct_no='+str (acct_no) )
                              data=cur.fetchall()
                              count=cur.rowcount
                              conn.commit()
                              if count == 0:
                                   print()
                                   print('Account Number Invalid Sorry Try Again Later')
                                   print()
                              else:
                                   print()
                                   print('1.WITHDRAW AMOUNT')
                                   print()
                                   print('2.ADD AMOUNT')
                                   print()

                                   print()
                                   x=int(input('Enter your CHOICE='))
                                   print()
                                   if x == 1:
                                        amt=int(input('Enter withdrawl amount='))
                                        cr_amt=0
                                        cur.execute('update customer_details2015 set   cr_amt=cr_amt-'+str(amt) +  ' where acct_no=' +str(acct_no) )
                                        V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),amt,cr_amt)
                                        cur.execute(  V_SQLInsert)
                                        conn.commit()
                                        print()
                                        print('Account Updated Succesfully!!!!!')



                                   if x== 2:
                                         amt=int(input('Enter amount to be added='))
                                         cr_amt=0
                                         cur.execute('update customer_details2015 set  cr_amt=cr_amt+'+str(amt) +  ' where acct_no=' +str(acct_no) )
                                         V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),cr_amt,amt)
                                         cur.execute(  V_SQLInsert)
                                         conn.commit()
                                         print()
                                         print('Account Updated Succesfully!!!!!')

                         if n == 3:
                              acct_no=int(input('Enter your account number='))
                              print()
                              cur.execute('select * from customer_details2015 where acct_no='+str(acct_no) )
                              if cur.fetchone() is  None:
                                   print()
                                   print('Invalid Account number')
                              else:
                                   cur.execute('select * from customer_details2015 where acct_no='+str(acct_no) )
                                   data=cur.fetchall()
                                   for row in data:
                                        print('ACCOUNT NO=',acct_no)
                                        print()
                                        print('ACCOUNT NAME=',row[1])
                                        print()
                                        print(' PHONE NUMBER=',row[2])
                                        print()
                                        print('ADDRESS=',row[3])
                                        print()
                                        print('cr_amt=',row[4])
                         if n == 4:
                               acct_no=int(input('Enter your account number='))
                               print()
                               cur.execute('select * from customer_details2015 where acct_no='+str(acct_no) )
                               if cur.fetchone() is  None:
                                   print()
                                   print('Invalid Account number')
                               else:
                                   cur.execute('select * from transactions where acct_no='+str(acct_no) )
                                   data=cur.fetchall()
                                   for row in data:
                                        print('ACCOUNT NO=',acct_no)
                                        print()
                                        print('DATE=',row[1])
                                        print()
                                        print(' WITHDRAWAL AMOUNT=',row[2])
                                        print()
                                        print('AMOUNT ADDED=',row[3])
                                        print()


                         if n == 5:
                              print('DELETE YOUR ACCOUNT')
                              acct_no=int(input('Enter your account number='))

                              cur.execute('delete from customer_details2015 where acct_no='+str(acct_no) )
                              print('ACCOUNT DELETED SUCCESFULLY')
                         if n == 6:
                           writeAccount()
                         if n == 7:
                             num = int(input("\tEnter The account No. : "))
                             depositAndWithdraw(num, 1)
                         if n == 8:
                               num = int(input("\tEnter The account No. : "))
                               depositAndWithdraw(num, 2)
                         if n == 9:
                             num = int(input("\tEnter The account No. : "))
                             displaySp(num)
                         if n == 10:
                               displayAll();
                         if n == 11:
                          num =int(input("\tEnter The account No. : "))
                          deleteAccount(num)
                         if n == 12:
                          num = int(input("\tEnter The account No. : "))
                          modifyAccount(num)
                         if n == 13:
                          print('DO YOU WANT TO EXPLORE MORE ABOUT YOUR ACCOUNT (y/n)')
                          c=input ('enter your choice=')




else:
     print('THANK YOU PLEASE VISIT YDS BANK AGAIN')
     quit()



import sqlite3
funn=sqlite3.connect('yashh.db')
ll=funn.cursor()

ll.execute=("create table Emp(empno int primary key, ename varchar(30), sal int, dno int);")
ll.execute=("create table Emp(empno int primary key, ename varchar(30), sal int, dno int);")
ll.execute("INSERT INTO employee values(1,'Aman',30000,2);")
ll.execute("SELECT * FROM employee;")
print(ll.fetchall())

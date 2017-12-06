from AccountScheduler import AccountScheduler
import re
from User import User
from Account import Account
from UserError import *
from random import *
from datetime import *


class Main:
    def __init__(self):
        self.__accountScheduler = AccountScheduler()

    def startSystem(self):
        while True:
            choice = input(
                "Enter your choice\n1. Create Account\n2. Deposit Amount\n3. Withdraw Amount\n4. Transfer Amount\n5. Exit\n")

            if choice == 1:
                user = User()
                while True:
                    try:
                        userName = raw_input("Enter username")
                        if re.match("^[a-zA-Z][a-zA-Z0-9]{2,15}$", userName) is None:
                            raise UserNameError(
                                "UserName should start with alphabet and can only have alphabets and digits")
                        elif not self.__accountScheduler.isUserNameAvailable(userName):
                            raise UserNameError("UserName already exists, choose other username")
                        user.setUserName(userName)
                        break
                    except UserNameError, userNameError:
                        print userNameError

                while True:
                    try:
                        userEmail = raw_input("Enter Email")
                        if re.match("^[a-zA-Z0-9.#$_]{3,}@[a-zA-Z]{2,10}.[a-z]{2,5}.?[a-z]{2,5}$", userEmail) is None:
                            raise UserEmailError("Please enter email in valid format")
                        user.setUserEmail(userEmail)
                        break
                    except UserEmailError, userEmailError:
                        print userEmailError

                accountNumber = randint(1, 100000)

                while True:
                    if self.__accountScheduler.isAccountNumberAvailable(accountNumber) is False:
                        user.setAccountNumber(accountNumber)
                        break
                    else:
                        accountNumber = (1, 100000)
                        continue

                self.__accountScheduler.createUser(user)

                account = Account()
                account.setUserName(userName)
                account.setAccountNumber(accountNumber)
                account.setAccountBalance(0)
                account.setAccountType("Savings")
                account.setAccountCreationDate(date.today())

                self.__accountScheduler.createAccount(account)

                print "Congratulations " + str(
                    userName) + "! Your account has been successfully created with accountNumber: " + str(accountNumber)

            elif choice == 2:
                while True:
                    try:
                        accountNumber = input("Enter your account Number")
                        break
                    except SyntaxError:
                        print "Account Number can be numeric only"

                while True:
                    try:
                        amount = input("Enter the amount you want to deposit")
                        if amount <= 0:
                            raise AmountError("Amount should be greater than zero")
                        break
                    except AmountError, amountError:
                        print amountError
                    except SyntaxError:
                        print "Amount can only be numeric"

                try:
                    print self.__accountScheduler.depositAmount(accountNumber, amount)
                except AccountNumberNotFoundError, accountNumberNotFoundError:
                    print accountNumberNotFoundError

            elif choice == 3:
                while True:
                    try:
                        accountNumber = input("Enter your account Number")
                        break
                    except SyntaxError:
                        print "Account Number can be numeric only"

                while True:
                    try:
                        amount = input("Enter the amount you want to withdraw")
                        if amount <= 0:
                            raise AmountError("Amount should be greater than zero")
                        break
                    except AmountError, amountError:
                        print amountError
                    except SyntaxError:
                        print "Amount can only be numeric"

                try:
                    print self.__accountScheduler.withdrawAmount(accountNumber, amount)
                except AccountNumberNotFoundError, accountNumberNotFoundError:
                    print accountNumberNotFoundError
                except InsufficientBalanceError, insufficientBalanceError:
                    print insufficientBalanceError

            elif choice == 4:
                while True:
                    try:
                        senderAccountNumber = input("Enter your account Number")
                        break
                    except SyntaxError:
                        print "Account Number can be numeric only"

                while True:
                    try:
                        receiverAccountNumber = input("Enter receiver account Number")
                        break
                    except SyntaxError:
                        print "Account Number can be numeric only"

                while True:
                    try:
                        amount = input("Enter the amount you want to Transfer")
                        if amount <= 0:
                            raise AmountError("Amount should be greater than zero")
                        break
                    except AmountError:
                        print AmountError.message
                    except SyntaxError:
                        print "Amount can only be numeric"

                try:
                    print self.__accountScheduler.transferFund(senderAccountNumber, receiverAccountNumber, amount)
                except AccountNumberNotFoundError, accountNumberNotFoundError:
                    print accountNumberNotFoundError
                except InsufficientBalanceError, insufficientBalanceError:
                    print insufficientBalanceError

            elif choice == 5:
                while True:
                    try:
                        accountNumber = input("Enter your account Number")
                        break
                    except SyntaxError:
                        print "Account Number can be numeric only"

                try:
                    transactions = self.__accountScheduler.getTransactionHistory(accountNumber)
                    if transactions is None:
                        print "You have not done any transactions yet"
                    else:
                        print "TransactionId     Transaction Description     Transaction Type     Account Numeber     Amount\n"
                        for transaction in transactions:
                            print str(transaction.getTransactionId()), str(
                                transaction.getTransactionDescription()), str(transaction.getTransactionType()), str(
                                transaction.getAccountNumber()), str(transaction.getTransactionAmount())
                except AccountNumberNotFoundError, accountNumberNotFoundError:
                    print accountNumberNotFoundError

            elif choice == 6:
                exit(0)

            else:
                print "Invalid Choice"


main = Main()
main.startSystem()

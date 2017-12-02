from Repository import Repository
from Transaction import Transaction
from random import *
from datetime import *
from UserError import *


class AccountScheduler:

    def __init__(self):
        self.__repository = Repository()

    def createAccount(self, account):
        self.__repository.addAccount(account)

    def createUser(self, user):
        self.__repository.addUser(user)

    def depositAmount(self, accountNumber, amount):

        if self.isAccountNumberAvailable(accountNumber) is False:
            raise AccountNumberNotFoundError("Entered Account Number does not exist")
        account = self.__repository.getAccount(accountNumber)
        account.setAccountBalance((account.getAccountBalance() + amount))
        self.__repository.updateAccount(account)

        transaction = Transaction()
        transId = randint(1,100000)
        while True:
            if self.isTransactionIdAvailable(transId) is True:
                transaction.setTransactionId(transId)
                break
            else:
                transId = randint(1,100000)
                continue

        transaction.setTransactionId(transId)
        transaction.setAccountNumber(accountNumber)
        transaction.setTransactionAmount(amount)
        transaction.setTransactionDescription("Deposited Amount")
        transaction.setTransactionType("Deposit")
        transaction.setTransactionDate(date.today())

        self.__repository.addTransaction(transaction)
        message = "Rs. " + str(amount) + " Deposited successfully in the account number: " + str(accountNumber)
        return message
    def withdrawAmount(self, accountNumber, amount):

        if self.isAccountNumberAvailable(accountNumber) is False:
            raise AccountNumberNotFoundError("Entered Account Number does not exist")

        account = self.__repository.getAccount(accountNumber)

        if account.getAccountBalance() < amount or (account.getAccountBalance() - amount) < 0:
            raise InsufficientBalanceError("Insufficient Balance: Cannot withdraw the entered amount")

        account.setAccountBalance((account.getAccountBalance() - amount))
        self.__repository.updateAccount(account)

        transaction = Transaction()
        transId = randint(1,100000)
        while True:
            if self.isTransactionIdAvailable(transId) is True:
                transaction.setTransactionId(transId)
                break
            else:
                transId = randint(1,100000)
                continue

        transaction.setTransactionId(transId)
        transaction.setAccountNumber(accountNumber)
        transaction.setTransactionAmount(amount)
        transaction.setTransactionDescription("Amount Withdraw from account")
        transaction.setTransactionType("Withdraw")
        transaction.setTransactionDate(date.today())

        self.__repository.addTransaction(transaction)
        message =  "Rs. " + str(amount) + " withdrawn successfully from the account number: " + str(accountNumber)
        return message

    def transferFund(self, senderAccountNumber, receiverAccountNumber, amount):

        if self.isAccountNumberAvailable(senderAccountNumber) is False:
            raise AccountNumberNotFoundError("Sender Account Number does not exist")

        if self.isAccountNumberAvailable(receiverAccountNumber) is False:
            raise AccountNumberNotFoundError("Receiver Account Number does not exist")

        senderAccount = self.__repository.getAccount(senderAccountNumber)
        receiverAccount = self.__repository.getAccount(receiverAccountNumber)

        if senderAccount.getAccountBalance() < amount:
            raise InsufficientBalanceError("Insufficient Balance: Cannot Transfer the entered amount")

        senderAccount.setAccountBalance((senderAccount.getAccountBalance() - amount));
        receiverAccount.setAccountBalance((receiverAccount.getAccountBalance() + amount));

        transaction = Transaction()
        transId = randint(1,100000)
        while True:
            if self.isTransactionIdAvailable(transId) is True:
                transaction.setTransactionId(transId)
                break
            else:
                transId = randint(1,100000)
                continue

        transaction.setTransactionId(transId)
        transaction.setAccountNumber(senderAccountNumber)
        transaction.setTransactionAmount(amount)
        transaction.setTransactionDescription("Amount Transferred")
        transaction.setTransactionType("Fund Transfer")
        transaction.setTransactionDate(date.today())
        self.__repository.addTransaction(transaction)

        while True:
            if self.isTransactionIdAvailable(transId) is True:
                transaction.setTransactionId(transId)
                break
            else:
                transId = randint(1,100000)
                continue

        transaction.setAccountNumber(receiverAccountNumber)
        transaction.setTransactionDescription("Amount Received")
        self.__repository.addTransaction(transaction)

        message =  "Rs. " + str(amount) + " transferred successfully from the account number: " + str(
            senderAccountNumber) + " to " + str(receiverAccountNumber)
        return message

    def isUserNameAvailable(self, userName):
        try:
            if self.__repository.getUser(userName) is None:
                return False
        except KeyError:
            return True

    def isAccountNumberAvailable(self, accountNumber):
        try:
            if self.__repository.getAccount(accountNumber) is not None:
                return True
        except KeyError:
            return False

    def isTransactionIdAvailable(self, transId):
        try:
            if self.__repository.getTransaction(transId) is not None:
                return True
        except KeyError:
            return False

    def getTransactionHistory(self, accountNumber):
        if self.isAccountNumberAvailable(accountNumber) is False:
            raise AccountNumberNotFoundError("Account Number Does not exist")

        return self.__repository.getTransaction(accountNumber)
from Repository import Repository
from Transaction import Transaction
from random import *
from datetime import *
from UserError import *


class AccountScheduler:

    def __init__(self):
        self.__repository = Repository()

    def depositAmount(self, accountNumber, amount):
        account = self.__repository.getAccount(accountNumber)
        if account is None:
            raise AccountNumberNotFoundError("Entered Account Number does not exist")

        account.setAccountBalance((account.getAccountBalance()+amount))
        self.__repository.updateAccount(account)

        transaction = Transaction()
        transId = randint
        while True:
            if self.__repository.getTransaction(transId) is None:
                transaction.setTransactionId(transId)
                break
            else:
                transId = randint
                continue

        transaction.setTransactionId(transId)
        transaction.setAccountNumber(accountNumber)
        transaction.setTransactionAmount(amount)
        transaction.setTransactionDescription("Deposited Amount")
        transaction.setTransactionType("Deposit")
        transaction.setTransactionDate(date.today())

        self.__repository.addTransaction(transaction)
        return "Rs. "+amount+" Deposited successfully in the account number: "+accountNumber

    def withdrawAmount(self, accountNumber, amount):
        account = self.__repository.getAccount(accountNumber)
        if account is None:
            raise AccountNumberNotFoundError("Entered Account Number does not exist")

        if account.getAccountBalance()<amount or (account.getAccountBalance()-amount)<0:
            raise InsufficientBalanceError("Insufficient Balance: Cannot withdraw the entered amount")

        account.setAccountBalance((account.getAccountBalance() - amount))
        self.__repository.updateAccount(account)

        transaction = Transaction()
        transId = randint
        while True:
            if self.__repository.getTransaction(transId) is None:
                transaction.setTransactionId(transId)
                break
            else:
                transId = randint
                continue

        transaction.setTransactionId(transId)
        transaction.setAccountNumber(accountNumber)
        transaction.setTransactionAmount(amount)
        transaction.setTransactionDescription("Amount Withdraw from account")
        transaction.setTransactionType("Withdraw")
        transaction.setTransactionDate(date.today())

        self.__repository.addTransaction(transaction)
        return "Rs. " + amount + " withdrawn successfully from the account number: " + accountNumber

    def transferFund(self,senderAccountNumber, receiverAccountNumber, amount):
        senderAccount = self.__repository.getAccount(senderAccountNumber)
        receiverAccount = self.__repository.getAccount(receiverAccountNumber)
        if senderAccount is None:
            raise AccountNumberNotFoundError("Sender Account Number does not exist")

        if receiverAccount is None:
            raise AccountNumberNotFoundError("Receiver Account Number does not exist")

        if senderAccount.getAccountBalance() < amount:
            raise InsufficientBalanceError("Insufficient Balance: Cannot Transfer the entered amount")

        

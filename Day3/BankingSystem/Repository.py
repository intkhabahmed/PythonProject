class Repositroy:

    def __init__(self):
        self.__users = {}
        self.__accounts = {}
        self.__transactions = {}

    def addAccount(self, account):
        self.__accounts.update({account.getAccountNumber(): account})

    def addUser(self, user):
        self.__users.update({user.getUserId(): user})

    def addTransaction(self, transaction):
        self.__transactions.update({transaction.getTransactionId(): transaction})

    def getAccounts(self):
        return self.__accounts

    def getUsers(self):
        return self.__users

    def getTransactions(self):
        return self.__transactions
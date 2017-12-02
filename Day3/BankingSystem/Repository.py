class Repository:

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

    def updateAccount(self, account):
        self.__accounts[account.getAccountNumber()] = account

    def updateUser(self, user):
        self.__users[user.getUserId()] =  user

    def getAccount(self, accountNumber):
        return self.__accounts[accountNumber]

    def getUser(self, userId):
        return self.__users[userId]

    def getTransaction(self, acccountNumber):
        transactions = []
        for transaction in self.__transactions.values():
            if transaction.getAccountNumber() == acccountNumber:
                transactions.append(transaction)

        return transactions
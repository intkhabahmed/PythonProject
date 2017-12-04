class Repository:

    def __init__(self):
        self.__accounts = {}
        self.__users = {}
        self.__transactions = {}

    def addAccount(self, account):
        self.__accounts.update({account.getAccountNumber(): account})

    def addUser(self, user):
        self.__users.update({user.getUserName(): user})

    def addTransaction(self, transaction):
        self.__transactions.update({transaction.getTransactionId(): transaction})
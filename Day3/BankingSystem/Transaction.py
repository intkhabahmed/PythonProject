class Transaction:

    def __init__(self):
        self.__transactionId = ""
        self.__transactionAmount = ""
        self.__transactionDescription = ""
        self.__transactionType = ""
        self.__transactionDate = ""
        self.__accountNumber = ""

    def getTransactionId(self):
        return self.__transactionId

    def getTransactionAmount(self):
        return self.__transactionAmount

    def getTransactionDescription(self):
        return self.__transactionDescription

    def getTransactionType(self):
        return self.__transactionType

    def getTransactionDate(self):
        return self.__transactionDate

    def getAccountNumber(self):
        return self.__accountNumber

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId

    def setTransactionAmount(self, transactionAmount):
        self.__transactionAmount = transactionAmount

    def setTransactionDescription(self, transactionDescription):
        self.__transactionDescription = transactionDescription

    def setTransactionType(self, transactionType):
        self.__transactionType = transactionType

    def setTransactionDate(self, transactionDate):
        self.__transactionDate = transactionDate

    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber
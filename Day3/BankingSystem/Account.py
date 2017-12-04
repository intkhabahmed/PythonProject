class Account:

    def __init__(self):
        self.__accountNumber = ""
        self.__accountType = ""
        self.__accountBalance = ""
        self.__accountCreationDate = ""

    def getAccountNumber(self):
        return self.__accountNumber

    def getAccountBalance(self):
        return self.__accountBalance

    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

    def setAccountType(self, accountType):
        self.__accountType = accountType

    def setAccountBalance(self, balance):
        self.__accountBalance = balance

    def setAccountCreationDate(self, creationDate):
        self.__accountCreationDate = creationDate
class Account:

    def __init__(self):
        self.__accountNumber = ""
        self.__accountType = ""
        self.__accountBalance = ""
        self.__accountCreationDate = ""
        self.__userName = ""

    def getAccountNumber(self):
        return self.__accountNumber

    def getAccountType(self):
        return self.__accountType

    def getAccountBalance(self):
        return self.__accountBalance

    def getAccountCreationDate(self):
        return self.__accountCreationDate

    def getUserName(self):
        return self.__userName

    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

    def setAccountType(self, accountType):
        self.__accountType = accountType

    def setAccountBalance(self, accountBalance):
        self.__accountBalance = accountBalance

    def setAccountCreationDate(self, accountCreationDate):
        self.__accountCreationDate = accountCreationDate

    def setUserName(self, userName):
        self.__userName = userName

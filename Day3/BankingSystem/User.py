class User:

    def __init__(self):
        self.__userId = ""
        self.__userName = ""
        self.__userEmail = ""
        self.__accountNumber = ""

    def getUserId(self):
        return self.__userId

    def getUserName(self):
        return self.__userName

    def getUserEmail(self):
        return self.__userEmail

    def getAccountNumber(self):
        return self.__accountNumber

    def setUserId(self, userId):
        self.__userId = userId

    def setUserName(self, userName):
        self.__userName = userName

    def setUserEmail(self, userEmail):
        self.__userEmail = userEmail

    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber
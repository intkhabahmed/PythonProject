class User:

    def __init__(self):
        self.__userName = ""
        self.__userEmail = ""
        self.__accountNumber = ""

    def getUserName(self):
        return self.__userName


    def getUserEmail(self):
        return self.__userEmail

    def getAccountNumber(self):
        return self.__accountNumber

    def setUserName(self, userName):
        self.__userName = userName

    def setUserEmail(self, userEmail):
        self.__userEmail = userEmail

    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

class User:

    def __init__(self):
        self.__accountNumber = ""
        self.__userName = ""
        self.__email = ""
        self.__mobileNumber = ""

    def getAccountNumber(self):
        return self.__accountNumber

    def getUserName(self):
        return self.__userName

    def getEmail(self):
        return self.__email

    def getMobileNumber(self):
        return self.__mobileNumber

    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

    def setUserName(self, userName):
        self.__userName = userName

    def setEmail(self, email):
        self.__email = email

    def setMobileNumber(self, mobileNumber):
        self.__mobileNumber = mobileNumber
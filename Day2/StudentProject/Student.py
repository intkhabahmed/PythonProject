class Student:
    def __init__(self):
        self.__rollNumber = ""
        self.__name = ""
        self.__courseNames = []

    def setName(self,name):
        self.__name = name

    def setRollNumber(self,rollNumber):
        self.__rollNumber = rollNumber

    def addCourses(self,courseName):
        self.__courseNames.append(courseName)

    def getName(self):
        return self.__name

    def getRollNumber(self):
        return self.__rollNumber

    def getCourses(self):
        return self.__courseNames
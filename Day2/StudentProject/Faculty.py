class Faculty:

    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__courseNames = []

    def setId(self, id):
        self.__id = id

    def setName(self,name):
        self.__name = name

    def addCourses(self,courseName):
        self.__courseNames.append(courseName)

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getCourses(self):
        return self.__courseNames
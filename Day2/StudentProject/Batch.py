class Batch:

    def __init__(self):
        self.__id = ""
        self.__courseName = ""
        self.__facultyName = ""
        self.__students = []

    def setId(self, id):
        self.__id = id

    def setCourseName(self, courseName):
        self.__courseName = courseName

    def setFacultyName(self, facultyName):
        self.__facultyName = facultyName

    def addStudents(self, studentName):
        self.__students.append(studentName)

    def getId(self):
        return self.__id

    def getCourseName(self):
        return self.__courseName

    def getFacultyName(self):
        return self.__facultyName

    def getStudents(self):
        return self.__students
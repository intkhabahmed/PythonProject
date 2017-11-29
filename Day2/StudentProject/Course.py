class Course:

    def __init__(self):
        self.__courseName = ""

    def addCourse(self,courseName):
        self.__courseName = courseName

    def getCourses(self):
        return self.__courseName
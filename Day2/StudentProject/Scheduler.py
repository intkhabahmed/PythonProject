from Student import Student


class Scheduler:
    def __init__(self):
        self.__students = {}
        self.__faculties = {}
        self.__batches = {}

    def addStudent(self,student):
        self.__students.update({student.getRollNumber() : student})

    def addFaculty(self,faculty):
        self.__faculties.update({faculty.getId() : faculty})

    def addBatch(self,batch):
        self.__batches.update({batch.getId() : batch})

    def validateRollNumber(self,rollNumber):
        if rollNumber in self.__students.keys():
            return True
        return False

    def getStudentByRollNumber(self, rollNumber):
        return self.__students[rollNumber]

    def showAllStudents(self):
        i = 1
        for student in self.__students.values():
            print "Student",(i)
            print("Roll No: ", student.getRollNumber())
            print("Name: ", student.getName())
            print("Courses: ", student.getCourses())
            print "\n"
            i += 1
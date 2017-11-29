from Scheduler import Scheduler
from Student import Student
from Faculty import Faculty
from Batch import Batch

class Admin:
    def __init__(self):
        self.__scheduler = Scheduler()

    def start(self):
        while True:
            action = input(
                "Enter your choice\n1. Add Student\n2. Show Students\n3. Add Faculty\n4. Add Batch\n5. Exit\n")

            if action == 1:
                quantity = input("How many students you want to add")
                for i in range(0, quantity):
                    print "Student", (i + 1)
                    student = Student()
                    student.setName(raw_input("Enter student name"))
                    while (True):
                        rollNumber = input("Enter roll number")
                        if self.__scheduler.validateRollNumber(rollNumber):
                            print "Roll Number already exists"
                            continue
                        else:
                            student.setRollNumber(rollNumber)
                            break
                    noOfCourses = input("How many course you want to attend")
                    for j in range(0, noOfCourses):
                        print "Course", (j + 1)
                        student.addCourses(raw_input("Enter courseName"))
                        self.__scheduler.addStudent(student)
                print "Students added successfully, what do you want to do now\n"

            elif action == 2:
                self.__scheduler.showAllStudents()

            elif action == 3:
                faculty = Faculty()
                faculty.setId(raw_input("Enter Faculty Id"))
                faculty.setName(raw_input("Enter Faculty Name"))
                noOfCourses = input("How many course you want to attend")
                for j in range(0, noOfCourses):
                    print "Course", (j + 1)
                    faculty.addCourses(raw_input("Enter courseName"))
                    self.__scheduler.addFaculty(faculty)

            elif action == 4:
                batch = Batch()
                batch.setId(raw_input("Enter Batch Id"))
                batch.setCourseName(raw_input("Enter Course Name"))
                batch.setFacultyName(raw_input("Enter Faculty Name"))
                noOfStudents = input("How many students you want to attend\n")
                self.__scheduler.showAllStudents()
                for j in range(0, noOfStudents):
                    print "Student", (j + 1)
                    while True:
                        rollNumber = input("Enter Student Roll Number to add")
                        if self.__scheduler.validateRollNumber(rollNumber):
                            batch.addStudents(self.__scheduler.getStudentByRollNumber(rollNumber))
                            break
                        else:
                            print "Entered rollNumber does not exists, Try Again"
                            continue
                            self.__scheduler.addBatch(batch)
                print "Batch created successfully"

            elif action == 5:
                exit(0)

admin = Admin()
admin.start()

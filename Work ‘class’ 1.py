class student:
    "Common base class for all student"
    stucount = 0
    
    def __init__(self, name="student", grade=1):
        self.name = name
        self.grade = grade
        student.stucount += 1
        
    def displayCount(self):
        print("Total Student: %d" % student.stucount)
    
    def printstudent(self):
        print("Name:", self.name, "\nGrade:", self.grade)
    
    # Getter Method Declaration
    def getstudent(self, parameterType):
        if parameterType == "Name":
            return self.name
        elif parameterType == "grade":
            return self.grade
        else:
            return "Data Not Found"
    
    # Setter Method Declaration
    def setstudent(self, name, grade):
        self.name = name
        self.grade = grade

student1 = student()

user_name = input("Please enter your name: ")
user_grade = input("Please enter your grade: ")

student1.setstudent(user_name, user_grade)
student1.printstudent()

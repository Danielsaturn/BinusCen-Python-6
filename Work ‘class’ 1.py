class student:
    "Common base class for all student"
    stucount = 0
    
    def __init__(self, name="student", umur=1):
        self.name = name
        self.umur = umur
        student.stucount += 1
        
    def displayCount(self):
        print("Total Student: %d" % student.stucount)
    
    def printstudent(self):
        print("Name:", self.name, "\nGrade:", self.umur)
    
    # Getter Method Declaration
    def getstudent(self, parameterType):
        if parameterType == "Name":
            return self.name
        elif parameterType == "grade":
            return self.umur
        else:
            return "Data Not Found"
    
    # Setter Method Declaration
    def setstudent(self, name, umur):
        self.name = name
        self.umur = umur

student1 = student()

user_name = input("Please enter your name: ")
user_umur = input("Please enter your grade: ")
student1.setstudent(user_name, user_umur)
student1.printstudent()

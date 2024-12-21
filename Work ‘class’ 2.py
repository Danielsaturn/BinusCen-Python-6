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

while (True):
    student1 = student()
    print("""===== OOP Program =====
    1. Declare Object
    2. Display Object
    3. Change Object Value
    4. Delete Object
    5. Exit Program """)
    user_menu = input("Please enter a number based on the menu above: ")
        
    if(user_menu == "1"):
        
        user_name = input("Please enter your name: ")
        user_grade = input("Please enter your grade: ")
        student1.setstudent(user_name, user_grade)
        student1.printstudent()
        
    elif(user_menu == "2"):
        
        student1.printstudent()
        student1.displayCount()
        
    else:
        print("Please enter the correct number provided in the menu")

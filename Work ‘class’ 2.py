class student:
    "Common base class for all student"
    
    def __init__(self, name="student", grade=1):
        self.name = name
        self.grade = grade
    
    def printstudent(self):
        print("Name:", self.name, "\nGrade:", self.grade)
    
    def getstudent(self, parameterType):
        if parameterType == "Name":
            return self.name
        elif parameterType == "grade":
            return self.grade
        else:
            return "Data Not Found"
    
    def setstudent(self, name, grade):
        self.name = name
        self.grade = grade
student1 = student()

while (True):
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
        student1 = student()
        student1.setstudent(user_name, user_grade)
        student1.printstudent()
        
    elif(user_menu == "2"):
        
        student1.printstudent()
        
    elif(user_menu == "3"):
        
        user_change = input("Please enter if you desire to change name (name) or grade (grade): ")
        student1 = student()
        
        if(user_change == "name"):
            user_name = input("Please enter the changed name: ")
            student1.setstudent(user_name, user_grade)
            student1.printstudent
        elif(user_change == "grade"):
            user_grade = input("Please enter the changed grade: ")
            student1.setstudent(user_name, user_grade)
            student1.printstudent
        else:
            print("Please enter the correct to change the grade or name!")
        
    elif(user_menu == "4"):
        
        user_name = "none"
        user_grade = "none"
        student1 = student()
        student1.setstudent(user_name, user_grade)
        student1.printstudent()
        
    elif(user_menu == "5"):
        
        print("This code has stopped, thank you for choosing Dan's name and grade recorder<3")
        break
        
    else:
        print("Please enter the correct number provided in the menu")

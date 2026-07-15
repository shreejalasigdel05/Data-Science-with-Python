#student management system
students={}
def add_student():
    while True:
        try:
            student_id=int(input("ID: "))
            if student_id in students:
                print("Student ID already exists.")
            else:
                break
        except ValueError: 
            print("Please enter a new integer ID")
    
    while True:
        Name=input("Name: ").strip()
        if Name=="":
            print("Name cannot be empty")
        elif not Name.isalpha():
            print("Name should contain only letters.")
        else:
            break

    while True:
        try:
            Age=int(input("Age: "))
            if Age<=0:
                print("Age must be greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter the valid age!!")
    
    while True:
        Course=input("Course: ").strip()
        valid_courses=["BIT","BCA","BHM","BBA","BIM"]
        if Course not in valid_courses:
            print("Invalid Course")
        else:
            break
        
    while True:
        try:
            Marks=float(input("Marks: "))
            if 0<=Marks<=100:
                break
            else:
                print("Marks must be between 0 and 100")
        except ValueError:
            print("Please enter a valid number")
    students[student_id]={
        "Name":Name,
        "Age":Age,
        "Course":Course,
        "Marks":Marks
        }
    print(f"\nStudent {Name} Added successfully")
    

def view_student():
    if students=={}:
        print("Students is empty")
    else:
        print("\n======STUDENT LIST======")
        for student_id,student in students.items():
            print(f'ID: {student_id}')
            print(f'Name: {student["Name"]}')
            print(f'Age: {student["Age"]}')
            print(f'Course: {student["Course"]}')
            print('-'*30)
def search_student():
    pass
def update_student():
    pass
def delete_student():
    pass
def show_topper():
    pass
def average_marks():
    pass
def pass_fail():
    pass

while True:
    print("========================\n")
    print("STUDENT MANAGEMENT SYSTEM")
    print("========================\n")
    print("1.Add Student\n2.View Student \n3.Search Student \n4.Update Student\n5.Delete Student\n6.Show Topper \n7.Average Marks \n8.Pass/Fail Count\n9.Exit")
    choice=int(input("Enter the choice: "))
    if choice==1:
        add_student()
    elif choice==2:
        view_student()
    elif choice==3:
        search_student()
    elif choice==4:
        update_student()
    elif choice==5:
        delete_student()
    elif choice==6:
        show_topper()
    elif choice==7:
        average_marks()
    elif choice==8:
        pass_fail()
    elif choice==9:
        break
    else:
        print("Please enter the valid choice!!")
    

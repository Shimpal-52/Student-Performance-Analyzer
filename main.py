import json
students = []
def add_student():
    print("\n---add student---")
    roll = int(input("Enter roll number:"))
    for s in students:
        if s["roll"] == roll:
            print("Student with this roll number already exists.")
            return
    name = input("Enter name:")

    n1 = int(input("Python marks:"))
    n2 = int(input("DSA marks:"))
    n3 = int(input("Operating system marks:"))

    total = n1+n2+n3
    average = total/3

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    student = {
        "roll": roll,
        "name": name,
        "Python": n1,
        "DSA": n2,
        "Operating system": n3,
        "average": average,
        "grade": grade,
        "total": total,

    }
    students.append(student)
    print("\nStudent Added Successfully!\n")

    #show all students
def show_student():
    if len(students) == 0:
        print("\nNo Student Found\n")
        return
        print("\n------Student Records-----")
        for s in students:
            print("----------")
            print("roll :", s["roll"])
            print("Name :", s["name"])
            print("Python :", s["Python"])
            print("DSA :", s["DSA"])
            print("Operating system :", s["Operating system"])
            print("Total :", s["total"])
            print("Average :", round(s["average"],2))
            print("Grade :",s["grade"])

            print("----------")
def search_student():
    roll = int(input("Enter roll number:"))
    found = False

    for s in students:
        if s["roll"] == roll:
            print("\nstudent found")
            print("name:", s["name"])
            print("total :", s["total"])
            print("average :", round(s["average"],2))
            print("grade :", s["grade"])
            found = True
            break
        if not found:
            print("student not found")
def search_by_name():
    name = input("Enter name:")
    found = False

    for s in students:
        if s["name"].lower() == name.lower():
            print("\nstudent found")
            print("roll :", s["roll"])
            print("total :", s["total"])
            print("average :", round(s["average"],2))
            print("grade :", s["grade"])
            found = True
            break
    if not found:
        print("student not found")
def sort_student():
    n = len(students)
    for i in range(n):
        for j in range(0, n-i-1):
            if students[j]["total"] < students[j+1]["total"]:
                students[j],students[j+1] = students[j+1], students[j]
                print("\nstudent sorted successfully\n")

def show_topper():
    if len(students) == 0:
        print("no student found")
        return
    topper = students[0]
    for s in students :
        if s["total"] > topper["total"]:
            topper = s
            print("\n-----TOPPER-----")
            print("name :", topper["name"])
            print("roll :", topper["roll"])
            print("marks :", topper["total"])
            print("grade:", topper["grade"])
def python_topper():
    if len(students) == 0:
        print("no student found")
        return
    topper = students[0]
    for s in students :
        if s["Python"] > topper["Python"]:
            topper = s
    print("\n-----PYTHON TOPPER-----")
    print("name :", topper["name"])
    print("roll :", topper["roll"])
    print("marks :", topper["Python"])
    print("grade:", topper["grade"])
def dsa_topper():
    if len(students) == 0:
        print("no student found")
        return
    topper = students[0]
    for s in students :
        if s["DSA"] > topper["DSA"]:
            topper = s
    print("\n-----DSA TOPPER-----")
    print("name :", topper["name"])
    print("roll :", topper["roll"])
    print("marks :", topper["DSA"])
    print("grade:", topper["grade"])
def os_topper():
    if len(students) == 0:
        print("no student found")
        return
    
    topper = students[0]
    for s in students :
        if s["Operating system"] > topper["Operating system"]:
            topper = s
    print("\n-----OPERATING SYSTEM TOPPER-----")
    print("name :", topper["name"])
    print("roll :", topper["roll"])
    print("marks :", topper["Operating system"])
    print("grade:", topper["grade"])
def class_average():
    total = 0
    for s in students:
        total += s["average"]
    class_avg = total / len(students)
    print("\n-----CLASS AVERAGE-----")
    print("Class average :", round(class_avg, 2))

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
        print("\nData saved successfully!\n")

def load_data():
    global students
    try:
        with open("students.json","r") as file:
            students=json.load(file)
    except:
            students=[]

def pass_fail():
    passed = 0
    failed = 0
    for s in students:
        if s["average"]>=40:
            passed+=1
        else:
            failed+=1
            print("Passed =", passed)
            print("Failed =", failed)
def grade_distribution():
    for s in students:
        print(s["name"], ":",s["grade"])
        
#main menu

while True:
    print("\n=====student performance analyzer=====")
    print("1. Add student")
    print("2. show student")
    print("3. search student")
    print("4. search by name")
    print("5. sort by marks")
    print("6. show topper")
    print("7. show python topper")
    print("8. show dsa topper")
    print("9. show operating system topper")
    print("10. show class average")
    print("11. pass/fail report")
    print("12. grade distribution")
    print("13. exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        search_by_name()
    elif choice == "5":
        sort_student()
    elif choice == "6":
         show_topper()
    elif choice == "7":
        python_topper()
    elif choice == "8": 
        dsa_topper()
    elif choice == "9":
        os_topper()
    elif choice == "10":
        class_average()
    elif choice == "11":
        pass_fail()
    elif choice == "12":
        grade_distribution()
    elif choice == "13":
        print("\nThank you!")
        break
    else:
        print("\ninvalid choice")



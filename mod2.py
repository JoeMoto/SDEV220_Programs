# Name: Joseph Moto
# File name: mod2.py
# Description: This app will take students' names and GPAs and determine if they qualify for the Dean's List or Honor Roll

print("Enter 'ZZZ' as last name to quit")
print()

while True:

    last_name = input("Enter the student's last name: ")
    
    if last_name == 'ZZZ':
        print("Program ended.")
        break
    
    first_name = input("Enter student's first name: ")
    
    gpa = float(input("Enter student's GPA: "))
    
    if gpa >= 3.5:
        print(first_name + " " + last_name + " has made the Dean's List.")
    
    if gpa >= 3.25:
        print(first_name + " " + last_name + " has made the Honor Roll.")
    
    if gpa < 3.25:
        print(first_name + " " + last_name + " does not qualify for Dean's List or Honor Roll.")
    
    print()
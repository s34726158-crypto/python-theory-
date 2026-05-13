name = input("Enter student name: ")
dob = input("Enter date of birth (DD/MM/YYYY): ")
regno = input("Enter register number: ")
department = input("Enter department: ")
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
m4 = float(input("Enter marks for subject 4: "))
m5 = float(input("Enter marks for subject 5: "))
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
if percentage >= 90:
    message = "Excellent Performance"
elif percentage >= 75:
    message = "Very Good"
elif percentage >= 60:
    message = "Good"
elif percentage >= 50:
    message = "Average"
else:
    message = "Needs Improvement"
print("\n----- Student Details -----")
print("Name:", name)
print("DOB:", dob)
print("Register Number:", regno)
print("Department:", department)
print("\nMarks:", m1, m2, m3, m4, m5)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Performance:", message)


def average(marks):
    return sum(marks) / len(marks)

marks = [85, 90, 78, 92, 88]
subjects = ["Math", "Physics", "Chemistry", "Python", "English"]

print("Marks:", marks)
print("Subjects:", subjects)
print("Average:", average(marks))
print(marks + [95, 70])   
print(marks * 2)           
print(subjects[2])      
print(subjects[1:4])       
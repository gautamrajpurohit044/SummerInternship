name = input("enter the name of student: ")
Class = int(input("enter the class of student: "))

total_marks = int(input("enter the total marks: "))


Math = int(input("enter the marks of maths : "))
english = int(input("enter the marks of english : "))
science = int(input("enter the marks of science : "))
social = int(input("enter the marks of social : "))
political = int(input("enter the marks of political  : " ,))

print(f"\nname of student = {name}")
print(f"class = {Class} th")
total_mark = Math + english + science + social + political
percentage = (total_mark / total_marks) * 100
print(f"total marks = {Math + english + science + social + political}")
print(f"percentage =  {(Math + english + science + social + political) / total_marks * 100} %")

if percentage > 60:
    print("\nGrade A")
elif percentage > 50:
    print("\nGrade B")
else :
    print("\nGrade C")
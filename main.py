from student import create_student
from result import add_marks, get_result, calculate_percentage

student = create_student("Amey", 101)

add_marks(student, "Maths", 78)
add_marks(student, "Science", 65)
add_marks(student, "English", 72)

percentage = calculate_percentage(student)
result = get_result(student)

print("Student Name:", student["name"])
print("Roll No:", student["roll_no"])
print("Percentage:", percentage)
print("Result:", result)

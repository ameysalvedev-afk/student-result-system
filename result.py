def add_marks(student, subject, marks):
    student["marks"][subject] = marks

def calculate_percentage(student):
    total = sum(student["marks"].values())
    return total / len(student["marks"])

def get_result(student):
    percentage = calculate_percentage(student)
    if percentage >= 40:
        return "Pass"
    else:
        return "Fail"

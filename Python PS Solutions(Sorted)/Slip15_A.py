class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

# Create a Student object
student = Student("Alice", 85)

# Print original values
print(f"Original Name: {student.student_name}, Original Marks: {student.marks}")

# Modify the attribute values
student.student_name = "Bob"
student.marks = 90

# Print modified values
print(f"Modified Name: {student.student_name}, Modified Marks: {student.marks}")

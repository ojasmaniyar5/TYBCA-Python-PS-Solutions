class Student:
    def __init__(self, roll_no, name, age, gender):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender

class Test(Student):
    def __init__(self, roll_no, name, age, gender, marks):
        super().__init__(roll_no, name, age, gender)
        self.marks = marks
    
    def display(self):
        total_marks = sum(self.marks)
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
        print(f"Marks: {self.marks}, Total Marks: {total_marks}")

# Creating three objects of Test class
student1 = Test(101, 'John', 18, 'Male', [85, 90, 88])
student2 = Test(102, 'Alice', 19, 'Female', [78, 82, 80])
student3 = Test(103, 'Bob', 18, 'Male', [92, 89, 95])

# Displaying details
student1.display()
student2.display()
student3.display()

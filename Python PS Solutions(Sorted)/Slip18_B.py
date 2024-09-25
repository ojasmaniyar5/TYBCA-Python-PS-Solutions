class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Employee(Person):
    def __init__(self, name, address, staff_id, salary):
        super().__init__(name, address)
        self.staff_id = staff_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Address: {self.address}, Staff ID: {self.staff_id}, Salary: {self.salary}")

# Create 'n' Employee objects
n = int(input("Enter the number of employees: "))
employees = []

for _ in range(n):
    name = input("Enter name: ")
    address = input("Enter address: ")
    staff_id = input("Enter staff ID: ")
    salary = float(input("Enter salary: "))
    employee = Employee(name, address, staff_id, salary)
    employees.append(employee)

# Display all employee details
print("\nEmployee Details:")
for emp in employees:
    emp.display_details()

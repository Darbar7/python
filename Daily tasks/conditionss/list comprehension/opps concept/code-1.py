# class - Employee
# class variable (company_name))
# instance variable (empid, emp_name, emp_salary, emp_dept)
# instance method (show the functionality of employee based on your understanding)
# class method (show the employee coompany name) T
# create atleat 2 object
# and get the output
class Employee:
    company_name = "Tech Solutions"  # Class variable

    def __init__(self, empid, emp_name, emp_salary, emp_dept):
        self.empid = empid  # Instance variable
        self.emp_name = emp_name  # Instance variable
        self.emp_salary = emp_salary  # Instance variable
        self.emp_dept = emp_dept  # Instance variable

    def show_employee_details(self):  # Instance method
        print(f"Employee ID: {self.empid}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_dept}")

    @classmethod
    def show_company_name(cls):  # Class method
        print(f"Company Name: {cls.company_name}")
# Create objects
employee1 = Employee(101, "Alice", 50000, "HR") 
employee2 = Employee(102, "Bob", 60000, "IT")
# Get output
employee1.show_employee_details()
employee2.show_employee_details()
Employee.show_company_name()

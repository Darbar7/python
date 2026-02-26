# class - Employee
# class variable (company_name))
# instance variable (empid, emp_name, emp_salary, emp_dept)
# instance method (show the functionality of employee based on your understanding)
# class method (show the employee coompany name) T
# create atleat 2 object
# and get the output

class Employee:
  company_name = "Tech Solutions"
  
  def __init__(self,empid,emp_name,emp_salary,emp_dept):
    self.empid = empid
    self.emp_name = emp_name
    self.emp_salary = emp_salary
    self.emp_dept = emp_dept

  def show_employee_functionality(self):
    print(f'Employee ID: {self.emp}')
    print(f'Employee name: {self.emp_name}')
    print(f'Employee salary: {self.emp_salary}')
    print(f'Employee depart: {self.emp_dept}')

 
  @classmethod
  def shoe_company_name(cls):
    print(f'company name: {cls.company_name}')
  
  employee1 = Employee(101,"ram",45000,"TL")
  employee2 = Employee(102,"sam",50000,"HR")


employee1.show_employee_functionality()
employee2.show_employee_functionality()
Employee.show_company_name()
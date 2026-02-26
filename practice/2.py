numbers = [1,2,3,4,5]

squared_list = []

for num in numbers:
 square = num ** 2
squared_list.append(square)

print(squared_list)

[1, 4, 9, 16, 25]


numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
prime = (i for i in numbers if i % 1 == 0)
print (prime)

#salary
salary = [1000,2000,3000,4000,5000]
salary_list = []
for i in salary:
  if i >= 3000:
    salary_list.append(i)
print(salary_list)

marks = [40,50,60,70,80]
result = ['pass' if mark > 40 else 'fail' for mark in marks]
print(result)

words =['fruit','python', 'data', 'machine_learning']
result = {i : len(i) for i in words}
print(result)

#Set comprehension

numbers = [1,2,2,2,3,3,4,4, 5, 5, 5, 5,6,6]
unique_num = {i for i in numbers}
unique_square = {i:i  ** 2 for i in numbers}
print(unique_num)
print(unique_square)

data = [10, None , 20, None, 30]
q= [i for i in data if i != None]
print(q)

## #Convert the celcius temperature into fahrenheit
celcius = [0, 10, 20, 34.5]
fahrenheit = [i * 9 / 5 + 32 for i in celcius]
print(fahrenheit)


celcius = [0, 10, 20, 34.5]
temp  = { i for i in celcius }
fahrenheit = {i:i * 9 / 5 + 32 for i in celcius}
print(fahrenheit)

#Use get output in list and dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)


def add (a,b):
  return a + b
print(add(2,3))


def greet ():
  print('hello')

greet()


#POSTIONAL ARUGMENT
def info (name,age):
  print(f'my name is {name} and  my age is {age}')
info('darbar',22)


#take price as user input and create a function with 18 % gst price
def gst():
  price = int(input('enter the price'))
  price_gst = price * 0.18
  total = price + price_gst
  print(total)
gst()



# Innomatics is located in Kukatpally
def info (place,):
  print(f"innomatics is located in {place}")
info('Kukatpally')

def area(name,area):
  print(f'my native place is {name} ,{area}')
area('kadapa','rayalaseema')



def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
even_or_odd(4)


# Define a function to get palindrome number or string (e.g., madam, dad, 1230,123210

def is_palindrome(s):
    s = str(s)
    return s == s[::-1]
is_palindrome("madam")
is_palindrome(12321)

# write a function to reverse a string without using slicing
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s  # Prepend each character to build the reversed string
    return reversed_s

# Test cases to demonstrate the corrected function
print(reverse_string("Hello World"))
print(reverse_string("madam"))
print(reverse_string("12345"))

def square (n):
  return n**2

square(5)


square = lambda x : x**2
square(5)

add = lambda x,y,z : x+y+z
add(4,5,6)

max = lambda a,b  : a if a>b else b
max(5,7)

min = lambda x,z : x if x<z else z
min(5,6)

num = lambda x :x if x%2 == 0 else "odd"
num (7)

num = lambda y : y if y % 2!=0 else "prime"
num (2)

#map
num1 = [1,2,3,4,5,6,7]
squared_numbers = list(map(lambda a : a**2,num1))
print(squared_numbers)

a = [12,31,43,34,32,42]
d = list(map(lambda a :a * a,a))
print(d)

c = ['banana','apple','grapes']
d = list(map(lambda c: c.title(),c ))

print(d)

c = ['banana','apple','grapes']
d = list(map(lambda c: c.upper(),c ))
print(d)


a = [1,2,34,45]
b = [1,34,43,56]
c = list(map(lambda a,b: a+b,a,b))
print(c)

a = [1]
x = [2]
# The filter function expects two arguments: a function and a single iterable.
# Here, it received three arguments: the lambda function, list 'a', and list 'x'.
# To compare elements from two lists, you should first combine them using zip().
# This creates an iterable of tuples, which can then be passed to filter.
filtered_elements = list(filter(lambda pair: pair[0] > pair[1], zip(a, x)))
print(filtered_elements)

num = [-1,2,3,-11,-22]
positive = list(filter(lambda num : num > 0,num))
negitive = list(filter(lambda num : num < 0,num))
print(positive)
print(negitive)

words = ['AI', 'DATA' , 'MACHINE LEARNING' , 'DEEP LEARNING' , 'PYTHON' ]
strings = list(filter (lambda words : len(words)> 3,words))
print(strings)


Emails = ['rohit123@gmail.com', 'abc@yahoo.com', 'amit.pal@gmail.com', 'riya.outlook.com']
mail = list(filter(lambda Emails : Emails.endswith("@gmail.com"),Emails))
print(mail)


# reduce function
from functools import reduce
nums = [1,2,3,4,5,6,7]
total = reduce(lambda c,d : c+d ,nums)
print(total)

nums = [5,10,15,20]
from functools import reduce
max = reduce(lambda x,c :x if x > c else c,nums)
print(max)

#zip function
name = ['zara','zudio','polo','style']
ratings = [5,4,3,4]
zipped = (list(zip(name,ratings)))
print(zipped)

#unzip
name,ratings = zip(*zipped)
print(list(name))
print(list(ratings))

class Animal:
  def __init__(self, name, voice, breed):
    self.name = name
    self.voice = voice
    self.breed = breed

  def Voice(self):
    return f'{self.name} does {self.voice}'

animal1 = Animal('Dog', 'Bark','German')
animal2 = Animal('Cat', 'Meow', 'Indian')

print(animal1.Voice())
print(animal2.Voice())

#classmethod

class student:
  collage = 'jntu'

  @classmethod
  def show_college(cls):
    print('college:',cls.collage)
student.show_college()

class Student:
  college = 'JNTU'

  @classmethod
  def show_college(cls):
    print('College:',cls.college)

Student.show_college()

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


class Student:
  def __init__(self, id, name, age, marks):
    self.id = id
    self.name = name
    self.age = age
    self.marks = marks

s1 = Student(101,'Rohan' ,25,79)

print(s1.name)

class Person:
  def __init__(self, Name, Age):
    self.Name = Name
    self._Age = Age

class Employee(Person):
  def display(self):
    print("Name:", self.Name)
    print("Age:", self._Age)

emp = Employee('rohan',25)
emp.display()

#private variable
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def show_balance(self):
        print('Balance:', self._balance)

acc = BankAccount(50000)
acc.show_balance()

#Private variable - Accessible only inside class  

class Student:
    def __init__(self):
        self._marks = 0 # Using _marks for convention

    #Setter method
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks # Corrected assignment
        else:
            print('Invalid marks')

    #Getter method
    def get_marks(self):
        return self._marks

stu = Student()

stu.set_marks(97)
print(stu.get_marks())

stu.set_marks(101) # Test invalid marks

#task - Create a BankAccount class
# account_holder is public
# balance is private
# Add methods to deposit, withdraw, and check balance
# Do not allow direct acces to balance

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public variable
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew: {amount}. New Balance: {self.__balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current Balance: {self.__balance}")
# Create an object of BankAccount
account = BankAccount("John Doe", 1000)
# Perform some operations   
account.check_balance()
account.deposit(500)    
account.withdraw(200)
account.check_balance()     
account.withdraw(1500)  # Attempt to withdraw more than balance
account.deposit(-100)  # Attempt to deposit a negative amount
account.withdraw(-50)  # Attempt to withdraw a negative amount

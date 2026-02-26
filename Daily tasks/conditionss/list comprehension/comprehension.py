# Create a new list where:
#even numbers are squared
#odd numbers are kept as-

numbers = [1, 2, 3, 4, 5, 6]
new_numbers = [num**2 if num % 2 == 0 else num for num in numbers]
print(new_numbers) 


#Create a list of words:
#having length ≥ 5
#converted to uppercase
words = ["hello", "world", "python", "is", "great"]
new_words = [word.upper() for word in words if len(word) >= 5]  
print(new_words)


#Use input() to take the start and end values from the user.
#Use a loop  to calculate the factorial of each number in the range.
#Remember: 0! is defined as 1.

start = eval(input())
end = eval(input())
for i in range (1, end+1):
    if i == 0:
        end = 1
    else:
        end *= i
print(end)


#Returning Multiple Values
# Write a function calculate(a, b) that returns both the sum and product of a and b. How do you capture both values?
def calculate(a, b):
    return a + b, a * b

sum_val, product_val = calculate(5, 3)
print("Sum:", sum_val)
print("Product:", product_val)
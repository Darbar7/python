# Define a function to get even or odd number
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
even_or_odd()

# Define a function to get palindrome number or string (e.g., madam, dad, 1230,123210321)
def is_palindrome(s):
    s = str(s)  
    return s == s[::-1]
is_palindrome("madam")  
is_palindrome(12321)

# Find a factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
factorial(5)

# write a function to reverse a string without using slicing
def reverse_string(s):
    words = int(input("Enter the number of words: "))
    reversed_string = ""
    for i in range(words):
        word = input("Enter word: ")
        reversed_string = word + " " + reversed_string
    return reversed_string.strip()
reverse_string("Hello World")

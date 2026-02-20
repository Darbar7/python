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






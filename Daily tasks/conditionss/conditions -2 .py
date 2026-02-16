##Create a program to check if the entered email is valid:
#Must contain @
#Must end with .com
#No starting blank spaces

email = input("enter your email:")
if email.startswith(" "):
    print("invalid email")
elif "@" not in email:
    print("invalid email")
elif not email.endswith(".com"):
    print("invalid email")
else:
    print("valid email")

#Test Cases:
#Input: john.doe@gmail.com ➞ Output: Valid Email
#Input: john@domain ➞ Output: Invalid Email
#Input: user@site.com ➞ Output:  valid Email

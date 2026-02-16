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

##Create a program to validate username format:
#Must start with a lowercase letter
#Can contain letters or  numbers or both 
#No symbols or spaces

user_name = input("enter user name:")
if user_name.startswith(" "):
    print("invalid")
elif user_name.lower():
    print("valid")
elif user_name.isalnum():
    print("valid")
else:
    print("invalid")
    


#Create a program to check if a word starts with a vowel:
#Vowels: a, e, i, o, u (case-insensitive)
#If it starts with a vowel ➞ Vowel Word
#Else ➞ Consonant Word
word = input("enter a word:")
if word.startswith(" "):
    print("invalid")    
elif word[0].lower() in "aeiou":
    print("Vowel Word")
else:
    print("Consonant Word")






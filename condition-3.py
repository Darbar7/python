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

     #Test Cases:
# Input: john123 ➞ Output: Username Accepted
 #Input: @john ➞ Output: Invalid Username
 #Input: JohnDoe ➞ Output: Invalid Username

 #Write a program to classify file type based on its extension:
#.pdf ➞ PDF File
#.docx ➞ Word File
#.xlsx ➞ Excel File
#Any other → Unknown Format
files = input("enter file format:")
if files.endswith(".pdf"):
  print("PDF File")
elif files.endswith(".docx"):
  print("Word File")
elif files.endswith(".xlsx"):
  print("Excel File")
else:
  print("Unknown Formate")

# Test Cases:
 #Input: report.pdf ➞ Output: PDF File
 #Input: resume.docx ➞ Output: Word File
 #Input: data.xls ➞ Output: Unknown Format

 #Create a program to detect if the input is blank or whitespace:
#Only whitespace → Blank Input
#Else → Input Received
input1 = input("enter input:")
if input1.strip() == '': # '' == ''
  print("Blank input")
else:
  print("input received")

# Test Cases:
 ##Input: " " ➞ Output: Blank Input
 #Input: " hello" ➞ Output: Input Received
 #Input: "\t\n" ➞ Output: Input Received

 #Create a program to check if a word is a properly formatted proper noun:
#Starts with capital letter
#Remaining letters are lowercase
name = input("enter word:")
if name.istitle():
  print("Proper Noun")
else:
  print("Incorrect Capitalization")

# Test Cases:
 #Input: India ➞ Output: Proper Noun
 #Input: india ➞ Output: Incorrect Capitalization
 #Input: INdia ➞ Output: Incorrect Capitalization

 #Write a program to validate a mobile number:
#Exactly 10 digits
#Only numeric characters allowed
number = int(input("enter mobile number:"))
if len(str(number)) == 10:
  print("valid")
else:
  print("invalid")

 # Test Cases:
 #Input: 9876543210 ➞ Output: Valid Number
 #Input: 123456789 ➞ Output: Invalid Number
 #Input: 12345abcde ➞ Output: Invalid Number


#Write a program to categorize a single character:
#Alphabet
#Digit
#Space
#Special Character


word = input("enter:")
if word.isalpha():
  print("Alphabet")
elif word.isdigit():
  print("Digit")
elif word.isspace():
  print("Space")
else:
  print("Special Character")


 #Test Cases:
 #Input: a ➔ Output: Alphabet
 #Input: 9 ➔ Output: Digit
 #Input: " " ➔ Output: Space
 #Input: # ➔ Output: Special Character

 #Identify the country based on phone number prefix:
#+91 ➞ India
#+44 ➞ UK
#Others ➞ Other


num = input("enter code:")
if num.startswith("+91"):
  print("India")
elif num.startwith("+41"):
  print("UK")
else:
  print("Other")


 #Test Cases:
 #Input: +919876543210 ➞ Output: India
 #Input: +441234567890 ➞ Output: UK
 #Input: +33123456789 ➞ Output: Other

 #Classify messages by urgency based on keywords:
#Contains urgent, immediately ➞ High Priority
#Contains report, update ➞ Informational
#Else ➞ Normal

user = input("enter your message:")
if "urgent" in user or "immediately" in user:
    print("High Priority")
elif "report" in user or "update" in user:
    print("Informational")
else:
    print("Normal")

 #Test Cases:
 #Input: This is urgent, please act now ➞ Output: High Priority
 #Input: Here is the report you requested ➞ Output: Informational
 #Input: Just checking in ➞ Output: Normal

 #Validate a coupon code using the following rules:
#Must start with "SAVE"
#Only alphanumeric characters allowed
coupon = input("enter cupon code:")
if coupon.startswith("SAVE") and "SAVE20A1" in coupon:
  print("Coupon Applied")
elif "SAVE201" in coupon:
  print("INvalid coupon")
else:
  print("invaid")


 #Test Cases:
 #Input: SAVE20A1 ➞ Output: Coupon Applied
 #Input: DISCOUNT ➞ Output: Invalid Coupon
 #Input: SAVE20!! ➞ Output: Invalid Coupon

 #Categorize a word based on its character count:
#Length ≤ 3 → Short
#Length 4–6 → Medium
#Length > 6 → Long

word = input("enter word:")
a=len(str(word))
if a <= 3:
  print("short")
elif a >= 4 and a <= 6:
  print("mediam")
else:
  print("long")

 #Test Cases:
 #Input: Cat ➞ Output: Short
 #Input: Book ➞ Output: Medium
 #Input: Elephant ➞ Output: Long

#Create a program to check if a word starts with a vowel:
#Vowels: a, e, i, o, u (case-insensitive)
#If it starts with a vowel ➞ Vowel Word
#Else ➞ Consonant Word

vowels = input("enter a vowels:")
if vowels.startswith(" "):
    print("invalid")
elif vowels[0].lower() in "aeiou":
    print("Vowel Word")
else:
    print("Consonant Word")


 #Test Cases:
 #Input: apple ➞ Output: Vowel Word
 #Input: Orange ➞ Output: Vowel Word
 #Input: banana ➞ Output: Consonant Word

 
user_name_input = input("Enter user name: ")
password_input = input("Enter the password: ")

user_name = "lucky"
password = "Lucky@123"

if user_name_input == user_name and password_input == password:
    print("Details matched")
else:
    print("Details not matched")

    #temperature
temperature = int(input("enter temperature:"))
if temperature > 25 :
  print("its summar")
else:
  print("its winter")

  # addendance & per%
students_attend = int(input("enter attend:"))
marks = float(input("marks:"))
percentage = marks % 100
if students_attend == 65 and percentage >= 90 :
   print ('grade A')
elif percentage >= 80:
   print ('grade b')
elif percentage >= 70:
   print ("c")
elif percentage >= 60:
   print ('d')
 
else:
   print ('fail')
   
   # only if
students_attend = int(input("Enter attendance: "))
marks = float(input("Enter marks: "))
percentage = marks / 100 * 10

if students_attend == 65 and percentage >= 90:
    if percentage >= 80:
        if percentage >= 70:
            if percentage >= 60:
                print('Grade FAIL')
            else:
                print('Grade D')
        else:
            print('Grade C')
    else:
        print('Grade B')
else:
    print('grade A')

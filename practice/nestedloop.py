# tables 
i = 2
while i <= 2:
    print("table of",i)
    j = 1
    while j <= 10:
        print(i,"*",j,"=",i*j)
        j+=1
    i+=1


# Check prime number
num = int(input("enter number:"))
while num > 1:
    if i % 1 ==0:
        print("prime number")
    else:
        print("not prime number")
    break

# Reverse a number
num = int(input("enter number:"))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10     


# Count digit in a number
num = int(input("enter number:"))
count = 0                           
while num > 0:
    num //= 10
    count += 1
print("number of digits:", count)


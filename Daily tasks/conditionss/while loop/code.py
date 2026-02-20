3.#Print Squares of Numbers from 1 to n
 #Ask the user for a number n, and use a while loop to print squares of numbers from 1 to n.
  #Input: 4
  #Output: 1 4 9 16
n = int(input("Enter a number: "))
i = 1   
while i <= n:
    print(i * i, end=' ')
    i += 1
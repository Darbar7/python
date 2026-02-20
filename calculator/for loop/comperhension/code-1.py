## #Convert the celcius temperature into fahrenheit
celcius = [0, 10, 20, 34.5]
fahrenheit = [i * 9 / 5 + 32 for i in celcius]

print(fahrenheit)



#Use get output in list and dictionary comprehension
#List comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers] 
print(squared_numbers)

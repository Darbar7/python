#task
# salary = [50000, 60000, 56000, 67000]
# give 15% hike
# salary, hiked_salary
#using for loop
salary = [50000, 60000, 56000, 67000]
hiked_salary = []
for i in salary:
    hiked_salary.append(i + (i * 15 / 100))
print("original salary:", salary)
print("hiked salary:", hiked_salary)



#Star pattern
# reverse star pattern

for i in range(6):
  i = i - 1
  for j in range(i):
    print("*", end="")
  print()
    

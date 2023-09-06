# write a program that determines whether a year entered by the user is a leap year or not using if-elif-else statement

year=int(input("Enter the year:"))

if(year%400==0) and (year%100==0):
  print(year,"is leap year")
elif(year%4==0) and (year%100 !=0):
  print(year,"is a leap year")
else:
  print(year,"is not leap year")
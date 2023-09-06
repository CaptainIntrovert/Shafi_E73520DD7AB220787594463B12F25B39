#implement a recursive function to calculate the factorial of a given number

def fact(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*fact(n-1)

num=int(input("Enter a number:"))
if(num<0):
  print("Factorial doesn't exist for negative number")
else:
  print("Factorial is ",fact(num))
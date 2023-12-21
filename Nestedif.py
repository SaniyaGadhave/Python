a=int(input("Enter the first number"))
b=int(input("Enter second number"))
c=int(input("Enter the third number"))
if a > b:
 if a > c:
  print("first number is greater")
if b > a:
 if b > c:
  print("second number is greater")
elif c > a:
 if c > b:
  print("third number is greater")
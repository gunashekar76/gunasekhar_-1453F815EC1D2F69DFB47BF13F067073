def recur_factorial(n):
  if n == 1:
    return n
  else:
    return n * recur_factorial(n - 1)


num = int(input("\n enter the number to find the factorial: "))
if num < 0:
  print("\n sorry,factorial does not exist for negative number")
elif num == 0:
  print("\n the factorial of 0 is 1")
else:
  print("\n The factorial of ", num, "is", recur_factorial(num))

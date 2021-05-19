# num = 0
# Function to calculate fibonacci numbers (regression method)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Function to calculate lucas numbers
def lucas(n):
  if n == 0:
    return 2
  if n == 1:
    return 1
  return lucas(n-1) + lucas(n-2)


# If no arguments are entered for i and j, it will return the Fibonacci number, otherwise, Lucas
def sum_series(n, i=0, j=1):
  if n == 0:
    return i
  if n == 1:
    return j
  return sum_series(n-1, i, j) + sum_series(n-2, i, j) 
    
# num = 0
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# for i in range(num):
#     print(fibonacci(i))

# num = 0
def lucas(n):
  if n == 0:
    return 2
  if n == 1:
    return 1
  return lucas(n-1) + lucas(n-2)
# for x in range(num):
#   print(lucas(x))

# num = 0

def sum_series(n, i=0, j=1):
  if n == 0:
    return i
  if n == 1:
    return j
  return sum_series(n-1, i, j) + sum_series(n-2, i, j) 
# print(sum_series(6))
    
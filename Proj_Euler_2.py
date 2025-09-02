# Every 3rd number in Fibonacci is even

def Fibonacci(limit):
  a, b = 0, 2 #first two even numbers
  totalsum=0
  while a < limit:
    totalsum += a
    a, b = b, 4 * b + a  #calculate next even fibonacci number
  return totalsum


result = Fibonacci(4000000)
print(result)

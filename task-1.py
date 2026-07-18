def caching_fibonacci():
  cache = {}
  def fibonacici(n):
    if n<=0:
      return 0
    if n == 1:
      return 1
    if n in cache:
      return cache[n]
    
    cache[n] = fibonacici(n-1)+fibonacici(n-2)
    return cache[n]
  return fibonacici

fib = caching_fibonacci()

print(fib(10))
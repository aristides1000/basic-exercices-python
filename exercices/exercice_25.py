def fib2(n=10): # devuelve la serie de Fibonacci hasta n
   """Devuelve una lista conteniendo la serie de Fibonacci"""
   result = []
   a, b = 0, 1
   while a < n:
      result.append(a)
      a, b = b, a+b
   print(result)

fib2(100)

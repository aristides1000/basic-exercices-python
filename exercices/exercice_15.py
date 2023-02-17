# Series de Fibonacci:
# la suma de dos elementos define el siguiente

# esto
a, b = 0, 1
# es lo mismo que esto:
# a = 0
# b = 1
while b < 100:
  print (b)
  # esto
  a, b = b, a+b
  # es lo mismo que esto:
  # a = b
  # b = a + b

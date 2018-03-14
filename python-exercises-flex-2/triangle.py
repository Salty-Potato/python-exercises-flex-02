   
triangle = int(input("How tall should the triangle be?  "))
for i in range(0, triangle):
   spaces = triangle - i - 1
   stars = i * 2 + 1
   print(' ' *spaces + "*" * stars)

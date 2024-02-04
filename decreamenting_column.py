n = 5 
for i in range(n): 
   p=65
   for j in range(i): 
      print(' ', end=' ') 
   for k in range(i, n):
      print(chr(p), end=' ')
      p+=1
   print()
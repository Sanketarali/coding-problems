n= 5 
k=69
for i in range(n): 
   p=k
   for j in range(i): 
      print(' ', end=' ') 
   for j in range(i, n):
      print(chr(p), end=' ')
      p-=1
   print()
   k-=1
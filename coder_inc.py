s = "CODER" 
n= len(s)
for i in range(n):
   p=0
   for j in range(i+1): 
      print(s[p], end=' ')
      p+=1
   print()

n = int(input("число: "))

def van(n):
   for i in range (n+1):
      yield i

fun = van(n)
for i in fun:
      
   print(i)

import math
c=0
n = 2147483647

sqrroot = int(math.sqrt(n))

for i in range (2,sqrroot):
    if (n % i == 0):
        c=c+1
        break
        
if c >0:
    print ("not prime")
else: 
    print ("prime")
            
                
                
        
        
   
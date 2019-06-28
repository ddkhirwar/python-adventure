# 6 digit biggest prime
import math
def isprime(n) :
    count = 0
    sqrtroot = int(math.sqrt(n))
    for i in (range(2,sqrtroot)) :
        if (n % i == 0):
            count = count+1
            
    if count==0:
        return True
    else:
        return False
    
        
print(isprime(999999))

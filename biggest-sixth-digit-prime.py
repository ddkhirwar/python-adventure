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

for n in reversed(range(100000,999999)):
    if isprime(n) == True :
        print ("biggest_six_digit_prime:"+str(n))
        break
        
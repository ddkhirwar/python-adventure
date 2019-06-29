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

no_of_digits = input("Enter the no of digits:")
no_of_digits = int(no_of_digits) -1
start_range = 10**no_of_digits
end_range = 10**(no_of_digits+1)-1

for n in reversed(range(start_range,end_range)):
    if isprime(n) == True :
        print ("biggest_six_digit_prime:"+str(n))
        break
        
from math import sqrt
import time


#n = int(input('Enter n: '))

start_range = 100
end_range = 1000

def primes_in_range(start_range, end_range):
    odd_check = False
    result = 0
    if start_range%2 == 0:
        start_range = start_range + 1
    for i in range(start_range, end_range+2, 2):
        if check_for_prime(i) :
            for j in range(0, len(str(i))):
                if(int(str(i)[j])%2==1):
                    odd_check = True
                else: 
                    break
            if odd_check == True:
                result = result + 1
    return result

def check_for_prime(n):
    prime = True
    if (n <=3 and n!=0):
        prime = True
    elif(n%2 ==0):
        prime = False
    else:
        for i in range(3, int(sqrt(n)) + 1, 2):
             if n % i == 0:
                prime = False
                break
    if prime:
        return True
    else:
        return False
   
print(primes_in_range(start_range, end_range))       
        
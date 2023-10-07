from math import sqrt
import time


n = int(input('Enter n: '))
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
    print('n is prime')
else:
    print('not prime')


    
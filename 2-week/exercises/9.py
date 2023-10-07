from math import sqrt
import time


a = int(input('Enter a: '))
b = int(input('Enter b: '))

start_range = a
end_range = b

def count_density(a,b):
    return ((b-a)+1)/check_for_number_of_prime_in_range(a, b)


def check_for_number_of_prime_in_range(start_range, end_range):
    count = 0
    if (start_range == 1 or start_range == 2):
        count = count + 1
    if start_range%2 == 0:
        start_range = start_range + 1
    for i in range(start_range, end_range, 2):
        if check_for_prime(i) :
            count = count + 1
        else:
            continue
    return count
        

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
   
print(count_density(a,b))       
        
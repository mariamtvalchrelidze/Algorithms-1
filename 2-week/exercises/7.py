from math import sqrt
import time


n = int(input('Enter n: '))

start_range = n
end_range = 2*n

def some_prime_in_range(start_range, end_range):
    result = 0
    if start_range%2 == 0:
        start_range = start_range + 1
    for i in range(start_range, end_range, 2):
        if check_for_prime(i) :
            result = i
            break
    return result

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

print("number of primes in given range: " + str(check_for_number_of_prime_in_range(start_range, end_range)))
print("some prime:" + str(some_prime_in_range(start_range, end_range)))

    
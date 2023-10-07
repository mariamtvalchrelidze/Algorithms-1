from math import sqrt
import time


n = int(input('Enter n: '))

f = 2
while n > 1:
    if n % f == 0:
        n = n // f
    else:
        f += 1

print(f)


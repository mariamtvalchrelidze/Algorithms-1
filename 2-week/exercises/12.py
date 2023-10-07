from math import sqrt
import time


n = int(input('Enter n: '))
count = 0
highest_fraq = 0
fraq = 0
f = 2
while n > 1:
    if n % f == 0:
        count = count + 1
        
        n = n // f
    else:
        if(count > highest_fraq):
            highest_fraq = count
            fraq = f
            count = 0
    
        
        f += 1
 
if n == 1:
    if(count > highest_fraq):
            highest_fraq = count
            fraq = f
    
print("number: " + str(highest_fraq))
print("fraq: " + str(fraq))

    
        




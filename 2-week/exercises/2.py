# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
N = int(input("Enter number: "))

def convert(N, s=''):
    if N == 0:
        return s
    else:
        d = N%2
        s = str(d) + s
        N=N//2
        return convert(N,s)
    
    
def check_heaviness(s):
    ones = 0
    zeroes = 0
    for i in range(0, len(s)):
        if s[i] =='1':
            ones = ones +1
        else:
            zeroes = zeroes + 1
    if zeroes > ones:
        return 'light'
    elif ones > zeroes:
        return 'heavy'
    else:
        return 'balanced'

print(check_heaviness(convert(N)))
            
            
        
    
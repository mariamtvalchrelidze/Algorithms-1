# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
N = int(input("Enter number: "))
#1634
def convert_seven_to_ten(N, s=''):
    max_power = len(str(N))-1
    res = 0 
    for i in range(0, len(str(N))):
        res = res + int(str(N)[i]) * 7**(max_power - i)
    return res

def convert_ten_to_three(N, s=''):
    if N == 0:
        return s
    else:
        d = N%3
        s = str(d) + s
        N=N//3
        return convert_ten_to_three(N,s)

def convert(N):
    return convert_ten_to_three(convert_seven_to_ten(N))
    

print(convert(N))   

            
            
        
    
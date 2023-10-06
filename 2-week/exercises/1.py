N = int(input("Enter number: "))

def convert(N):
    s = ''
    while N > 0:
        d = N % 2
        s = str(d) + s
        N = N // 2
    return s


while N > 0:
    print(convert(N))
    N = N - 1
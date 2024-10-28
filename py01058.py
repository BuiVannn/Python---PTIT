import math

def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    
    return n > 1

def solve(n):
    m = n[-4 : -1] + n[-1]
    m = int(m)
    if nt(m):
        return 1
    return 0

for _ in range(int(input())):
    n = input()
    if solve(n):
        print("YES")
    else:
        print("NO")
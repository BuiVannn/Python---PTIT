
import math

def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
        
    return n > 1

for _ in range(int(input())):
    n = input()
    ok = 1
    for i in range(len(n)):
        if nt(int(i)) and not nt(int(n[i])):
            ok = 0
            break
        if not nt(int(i)) and nt(int(n[i])):
            ok = 0
            break
    if ok:
        print("YES")
    else:
        print("NO")
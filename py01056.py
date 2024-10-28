
import math

def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1

def check(n):
    sum = 0
    for i in range(len(n)):
        if i % 2 == 0:
            if int(n[i]) % 2 != 0:
                return 0
        else:
            if(int(n[i]) % 2 == 0):
                return 0
        sum += int(n[i])
    if not nt(sum) :
        return 0
    return 1

for t in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")

import math

t = int(input())

def nt(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
        
    return n > 1

while t != 0:
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 3 == 0 :
        print("YES")
    else:
        print("NO")
    t -= 1
import math

def sum(n):
    s = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            s += i
            n //= i
    if n > 1:
        s += n
    return s

res = 0

for _ in range(int(input())):
    n = int(input())
    res += sum(n)

print(res)
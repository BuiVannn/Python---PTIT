mod = 1000000007
def pow(a : int, b: int):
    if b == 1: return a
    if b & 1: return pow(a, b - 1) * a % mod
    p = pow(a, b >> 1)
    return p * p % mod

def cal(n : int, k : int):
    if k <= 1: return k
    ex = 0
    while (k >> ex) ^ 1:
        ex += 1
    return pow(n, ex) + cal(n, k ^ (1 << ex))


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(cal(n, m) % mod)


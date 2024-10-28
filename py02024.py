
def tich(n):
    s = 1
    while n != 0:
        s *= (n % 10)
        n //= 10
    return s

for _ in range(int(input())):
    n, a = input(), input().split()
    n = int(n)
    a = [int(x) for x in a]
    b = sorted(a, key= lambda x : (tich(x), x))
    for i in b: 
        print(i, end=" ")
    print("")
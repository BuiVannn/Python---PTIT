def sum(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s

for _ in range(int(input())):
    n = input()
    a = input().split()
    a = [int(x) for x in a]
    b = sorted(a, key = lambda x : (sum(x), x))

    for i in b:
        print(i, end=" ")
    print("")
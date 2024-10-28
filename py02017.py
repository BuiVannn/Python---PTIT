
for _ in range(int(input())):
    n = int(input())
    d = dict({})
    a = list(input().split())

    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    for i in d:
        if d[i] % 2 != 0:
            print(i)
            break
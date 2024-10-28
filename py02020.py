n, a = input(), input().split()

n = int(n)

a = [float(x) for x in a]

a.sort()

b = a[0]
c = a[n - 1]

s = 0
cnt = 0
for i in a:
    if i != b and i != c:
        s += i
        cnt += 1
print("{:.2f}".format(s / cnt))

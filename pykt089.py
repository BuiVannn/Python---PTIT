
n = int(input())

#a = list(map(int, input().split()))
a = []
while len(a)<n:
    a.extend(list(map(int, input().split())))

b = []
c = []
for i in range(n):
    if a[i] % 2 != 0:
        b.append(i)
        c.append(a[i])

c.sort(reverse=True)
h = 0
for i in range(len(b)):
    a[b[i]] = c[i]
    h += 1

e = []
f = []
for i in range(n):
    if a[i] % 2 == 0:
        e.append(i)
        f.append(a[i])

f.sort()
h = 0
for i in range(len(e)):
    a[e[i]] = f[i]
    h += 1
for i in a:
    print(i, end=" ")
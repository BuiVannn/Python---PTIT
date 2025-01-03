
n = int(input())

#a = list(map(int, input().split()))
a = []
while len(a)<n:
    a.extend(list(map(int, input().split())))
goc = []
chan = []
le = []
for i in range(n):
    if a[i] % 2 == 0:
        chan.append(a[i])
        goc.append(0)
    else:
        le.append(a[i])
        goc.append(1)

chan.sort()
le.sort(reverse=True)

u = 0
v = 0
for i in range(n):
    if goc[i] == 0:
        #if u < len(chan):
            print(chan[u], end=' ')
            u += 1
    else:
        #if u < len(le):
            print(le[v], end=' ')
            v += 1


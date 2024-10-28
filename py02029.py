
n, k = map(int,input().split())

a = list(input().split())
d = dict({})

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

b = sorted(a)
res = d[b[0]]
for i in range(1, len(b)):
    if d[b[i]] > res:
        res = d[b[i]]
ans = -1
for i in range(n):
    if d[b[i]] > ans and d[b[i]] != res:
        ans = d[b[i]]
ok = 1
if ans == -1:
    ok = 0
else:
    for i in b:
        if d[i] == ans:
            ans = i
            break
if ok == 0:
    print("NONE")
else:
    print(ans)
def tohop(n):
    return (n * (n - 1)) // 2
n = int(input())

a = [[0 for _ in range(n)] for _ in range(n)]
c = [[0 for _ in range(200)] for _ in range(200)]

for i in range(n):
    a[i] = list(input())
ans = 0

for i in range(n):
    cnt = 0
    for j in range(n):
        if a[i][j] == 'C':
            cnt += 1
            
    #print(cnt)
    ans += tohop(cnt)
    #print('ans = ', ans)

for i in range(n):
    cnt = 0
    for j in range(n):
        if(a[j][i] == 'C'):
            cnt += 1
    #print(cnt)
    ans += tohop(cnt)
    #print('ans = ', ans)

print(ans)
#print(tohop(3))


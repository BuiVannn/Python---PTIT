
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    #n, s = input().split()
    q = input()
    #print(q)
    #print(len(q))
    if q == '0':
        break
    else:
        n, s = q.split()
        #print(n, s)
        n = int(n)
        s = list(s)
            #P[(i+K)%28]
        for i in range(len(s)):
            k = 0
            for l in range(len(P)):
                if P[l] == s[i]:
                    k = l
                    break
            s[i] = P[(k + n) % 28]
        ans = s[::-1]
        res = ""
        for i in ans:
            res += i
            #ans = str(ans)
        print(res)
        
    
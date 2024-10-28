
for _ in range(int(input())):
    n = input()
    arr = input().split()
    m = {}
    def c(a):
        for i in a:
            if(a[i] > int(int(n) / 2)):
                return i
        return 'NO'
    for x in arr:
        try: m[x] += 1
        except: m[x] = 1
    print(c(m))
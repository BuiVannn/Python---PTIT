from collections import Counter


for _ in range(int(input())):
    n, m, k = map(int, input().split())

    ok = False

    a = Counter([int(i) for i in input().split()])
    b = Counter([int(i) for i in input().split()])
    c = Counter([int(i) for i in input().split()])
    for x in a.keys():
        print(x)
    for x in a.values():
        print(x)

'''
    for x in a.keys():
        if x in b.keys() and x in c.keys():
            for i in range(min(a[x], min(b[x], c[x]))):
                ok = True
                print(x, end=' ')

                
    print('' if ok == True else "NO")
'''
    
    
    


from math import *

a = list(map(int,input().split()))

while not(a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0):
    tmp1 = a[0]
    ok1 = 1
    for i in range(1, 4):
        if a[i] != tmp1:
            ok1 = 0
            break
    if ok1 == 1:
        print(0)
    else:     
        cnt = 0 
        ok = 1
        while True :
            p = a[0]
            for i in range(3):
                a[i] = abs(a[i] - a[i + 1])

            a[3] = abs(a[3] - p)
            ok = 1
            tmp = a[0]
            for i in range(1, 4):
                if a[i] != tmp:
                    ok = 0
                    break
            cnt += 1
            if ok == 1:
                break
        print(cnt)
    a = list(map(int,input().split()))
    
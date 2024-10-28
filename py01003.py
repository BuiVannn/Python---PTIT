import math

n = int(input())
tmp = n


while n != 0:
    a = int(input())
    c = 0
    cnt = 0
    nho = 0
    while a != 0 :
        c = a % 10
        c += nho
        nho = 0
        a //= 10
        if c >= 5:
            nho = 1
        cnt += 1
    #print(int(math.pow(10, cnt - 1)))
    #print(c)
    #print(nho)
    print(c * int(math.pow(10, cnt - 1)))
    
    n -= 1
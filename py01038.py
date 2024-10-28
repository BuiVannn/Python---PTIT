t = int(input())

def rev(n):
    n1 = 0
    while n!= 0:
        n1 = n1 * 10 + n % 10
        n //= 10
    return n1
while t != 0:
    n = int(input())
    cnt = 0
    n1 = rev(n)
    while cnt <= 1000:
        if n % 7 == 0:
            print(n)
            break
        else:
            n1 = rev(n)
            n += n1
        cnt += 1
    #print(n1)
    t -= 1
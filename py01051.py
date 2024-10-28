t = int(input())

def check(n):
    tmp = 0
    m = n
    while n != 0:
        tmp = tmp * 10 + n % 10
        n //= 10 
    if m == tmp:
        return 1
    return 0

while t != 0:
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if check(sum) and sum >= 10:
        print("YES")
    else:
        print("NO")
    t -= 1
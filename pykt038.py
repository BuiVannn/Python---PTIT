import math

def chuyen(c, b ,a):
    s = math.pow(2, 2) * a + math.pow(2, 1) * b + c
    return s

n = input()
a = []
n = n[::-1]
for i in range(0, len(n), 3):
    if i + 2 < len(n):
        s = math.pow(2, 2) * int(n[i + 2]) + math.pow(2, 1) * int(n[i +1]) + int(n[i])
    elif i + 1 < len(n):
        s = math.pow(2, 1) * int(n[i +1]) + int(n[i])
    else:
        s = int(n[i])

    a.append(s)
ans = a[::-1]
for i in ans:
    print(int(i), end='')

n = int(input())

cnt = 0
while n != 0:
    c = n % 10
    if c == 4 or c == 7:
        cnt += 1
    n //= 10
if cnt == 4 or cnt == 7:
    print("YES")
else: print("NO")
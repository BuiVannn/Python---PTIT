
fb = [0] * 94

def solve():
    fb[1] = 1
    fb[2] = 1
    for i in range(3, 94):
        fb[i] = fb[i - 1] + fb[i - 2]

solve()
for _ in range(int(input())):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        print(fb[i], end=" ")
    print()
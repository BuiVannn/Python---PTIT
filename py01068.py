n, k = map(int, input().split())
x = input().split()
y = []
for i in x:
    if i not in y:
        y.append(i)
y = sorted(y)

def xuat(a, b):
    for i in a:
        print(b[i - 1], end=' ')
    print()


def sinh(n, k):
    a = list(range(1, k + 1))

    while True:
        xuat(a, y)
        #print(a)
        i = k - 1
        while i >= 0 and a[i] == n - k + i + 1:
            i -= 1
        
        if i < 0:
            break

        a[i] += 1

        for j in range(i + 1, k):
            a[j] = a[j - 1] + 1

sinh(len(y), k)

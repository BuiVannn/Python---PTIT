a = []

for i in range(int(input())):
    a.append(input())

while len(a) > 0:
    idx = len(a)
    for i in range(len(a)):
        if a[i] == '':
            idx = i
            break
    print("{}: {}".format(a[0], idx - 1))
    a = a[idx + 1:]
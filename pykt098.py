
f = open('DATA.in', 'r')

a = []

for line in f:
    b = line.strip().split()
    for i in b:
        x = 0
        try:
            x = int(i)
            if x > (1<<63):
                a.append(i)
        except:
            a.append(i)

a = sorted(a)
for i in a:
    print(i, sep=' ')
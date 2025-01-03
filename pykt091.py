
def check(s):
    u = s[::-1]
    if u == s:
        return True
    return False
f = open('VANBAN.in', 'r')

a = dict()

dainhat = -1e9
for line in f:
    b = line.strip().split()
    for i in b:
        if check(i):
            dainhat = max(dainhat, len(i))
            if a.get(i) == None:
                a[i] = 1
            else:
                a[i] += 1  

for key, value in a.items():
    if len(key) == dainhat:
        print(f'{key} {value}')


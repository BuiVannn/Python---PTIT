n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

class Mua:
    def __init__(self, truoc, sau):
        self.truoc = truoc
        self.sau = sau
        self.kc = self.truoc - self.sau


ds = []
for i in range(len(a)):
    ds.append(Mua(a[i], b[i]))

ds = sorted(ds, key=lambda x : x.kc)
tien = 0
for i in range(k):
    tien += ds[i].truoc
idx = k
while idx < n and ds[idx].truoc < ds[idx].sau:
    tien += ds[idx].truoc
    idx += 1

for j in range(idx, n):
    tien += ds[j].sau

print(tien)
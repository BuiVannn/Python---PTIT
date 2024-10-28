a, k, n = input().split()

a = int(a)
k = int(k)
n = int(n)

ok = 1

for i in range(a + k - (a % k), n + 1, k):
    ok = 0
    print(i - a, end=' ')

if ok: print(-1)
'''
a,k,n = map(int,input().split()) 
b = [] 
st = k -(a%k) 
end = n - a 
while st<=end: 
    b.append(str(st)) 
    st+=k 
    if(len(b)==0): 
        print(-1) 
    else: print(' '.join(b))
'''
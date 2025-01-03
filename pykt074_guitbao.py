t = int(input())

for i in range(t):
    a = input()
    if len(a) < 100:
        print(a)
    else:
        k = 98
        while a[k].isalpha():
            k -= 1
    
        print(a[:k])
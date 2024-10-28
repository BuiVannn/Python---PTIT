t = int(input())

while t != 0:
    n = input()
    a = n[0]
    b = n[1]
    if(a == b):
        print("NO")
    
    else:
        ok = 1
        for i in range(1, len(n)):
            if n[i] == n[i - 1] or( n[i] != a and n[i] != b):
                ok = 0
                break
        if ok:
            print("YES")
        else:
            print("NO")
    t -= 1
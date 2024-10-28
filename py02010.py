n = int(input())

while True:
    a = []
    while n != 0:
        a.append(int(input()))
        n -= 1
    
    a.sort()
    if a[0] == a[len(a) - 1]:
        print("BANG NHAU")
    else:
        print(a[0], a[len(a) - 1])
    
    n = int(input())
    if n == 0:
        break
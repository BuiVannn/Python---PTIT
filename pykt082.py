for _ in range(int(input())):
    a, b, c, d = map(float, input().split())
    a1 = 0
    b1 = 0
    if a == 3 or a == 4:
        a1 = 2.5
    elif a == 5 or a == 6:
        a1 = 3.0
    elif a >= 7 and a <= 9:
        a1 = 3.5
    elif a >= 10 and a <= 12:
        a1 = 4.0
    elif a >= 13 and a <= 15:
        a1 = 4.5
    elif a >= 16 and a <= 19:
        a1 = 5.0
    elif a >= 20 and a <= 22:
        a1 = 5.5
    elif a >= 23 and a <= 26:
        a1 = 6.0
    elif a >= 27 and a <= 29:
        a1 = 6.5
    elif a >= 30 and a <= 32:
        a1 = 7.0
    elif a >= 33 and a <= 34:
        a1 = 7.5
    elif a >= 35 and a <= 36:
        a1 = 8.0
    elif a >= 37 and a <= 38:
        a1 = 8.5
    elif a >= 39 and a <= 40:
        a1 = 9.0
    

    if b == 3 or b == 4:
        b1 = 2.5
    elif b == 5 or b == 6:
        b1 = 3.0
    elif b >= 7 and b <= 9:
        b1 = 3.5
    elif b >= 10 and b <= 12:
        b1 = 4.0
    elif b >= 13 and b <= 15:
        b1 = 4.5
    elif b >= 16 and b <= 19:
        b1 = 5.0
    elif b >= 20 and b <= 22:
        b1 = 5.5
    elif b >= 23 and b <= 26:
        b1 = 6.0
    elif b >= 27 and b <= 29:
        b1 = 6.5
    elif b >= 30 and b <= 32:
        b1 = 7.0
    elif b >= 33 and b <= 34:
        b1 = 7.5
    elif b >= 35 and b <= 36:
        b1 = 8.0
    elif b >= 37 and b <= 38:
        b1 = 8.5
    elif b >= 39 and b <= 40:
        b1 = 9.0
    
    dtb = (a1 + b1 + c + d) / 4
    res = int(dtb)
    du = dtb - res
    if du < 0.25:
        res += 0
    elif du >= 0.75:
        res += 1
    if du >= 0.25 and du < 0.75:
        res += 0.5
    print("{:.1f}".format(res))


for _ in range(int(input())):
    s = input()
    n = 0
    a = [""] * len(s)
    for i in s:
        if i.isalpha():
            a.append(i)
        if i.isdigit():
            n += int(i)
    a.sort()
    for i in a:
        if i != "":
            print(i, end="")
    #print(a)
    print(n)

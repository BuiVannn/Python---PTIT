s = input()

pos = 0
n = len(s)

while pos < n:
    tmp = s[pos]
    last_pos = pos
    for i in range(pos, n):
        if s[i] > tmp:
            tmp = s[i]
    
    for i in range(pos, n):
        if s[i] == tmp:
            print(s[i], end="")
            last_pos = i
    
    pos = last_pos + 1
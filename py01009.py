s = input()

n1 = 0
n2 = 0
for i in s:
    if i >= 'a' and i <= 'z':
        n1 += 1
    elif i >= 'A' and i <= 'Z':
        n2 += 1
if n1 >= n2:
    s1 = s.lower()
    print(s1)
else: 
    s1 = s.upper()
    print(s1)
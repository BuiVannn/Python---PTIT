

s = input()

if "688" in s:
    s = s.replace("688", "z")
if "68" in s:
    s = s.replace("68", "z")
if "6" in s:
    s = s.replace("6", "z")

ok = 1
for i in s:
    if i != 'z':
        ok = 0
if ok:
    print("YES")
else:
    print("NO")
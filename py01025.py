s = input()
cnt = 0
ans = ""
n = len(s) - 1
res = s[::-1]
for i in range(len(s)):
    if i % 3 == 0 and i != 0:
        ans += ","
    ans += res[i]
ans1 = ans[::-1]
print(ans1)
#153920529
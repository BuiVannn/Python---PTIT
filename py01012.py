s = input()
s1 = input()

n = int(input())

for i in range(0, n - 1):
    print(s[i], end="")

for i in s1:
    print(i, end="")

for i in range(n - 1, len(s)):
    print(s[i], end="")
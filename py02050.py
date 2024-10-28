def solve(a):
    n = len(a)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and a[stack[-1]] > a[i]:
            stack.pop()
        if stack:
            result[i] = i - stack[-1]
        else:
            result[i] = i + 1
        stack.append(i)
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    #ans = solve(a)
    result = []
    stack = []
    for i in range(n):
        while len(stack) > 0 and a[i] >= a[stack[-1]]:
            stack.pop()
        if len(stack) != 0:
            result.append( i - stack[-1])
        else:
            result.append(i + 1)
        stack.append(i)
    for i in result:
        print(i, end=' ')
    print()
            
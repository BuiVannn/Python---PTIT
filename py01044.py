line1 = input().lower().strip().split()
line2 = input().lower().strip().split()

hop = sorted(set(line1) | set(line2))
giao = sorted(set(line1) & set(line2))

print(' '.join(hop))
print(' '.join(giao))


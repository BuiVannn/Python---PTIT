n, m = map(int, input().split())

# Đọc danh sách a và b
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

# Tìm tập hợp chung và phần không chung
s1 = set(a)
s2 = set(b)

common = sorted(s1 & s2)  # Các phần tử chung
unique_a = [i for i in a if i not in common]  # Phần tử chỉ có trong a
unique_b = [i for i in b if i not in common]  # Phần tử chỉ có trong b

unique_a = sorted(unique_a)
unique_b = sorted(unique_b)
# In kết quả
print(" ".join(map(str, common)))  # In các phần tử chung
print(" ".join(map(str, unique_a)))  # In các phần tử chỉ có trong a
print(" ".join(map(str, unique_b)))  # In các phần tử chỉ có trong b

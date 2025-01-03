def convert(n, k):
    s = []
    while n != 0:
        d = n % k
        if d <= 9:
            s.append(str(d))  # Chuyển `d` thành chuỗi
        else:
            s.append(chr(65 + d - 10))  # Chuyển `d` thành ký tự chữ cái (A, B, C,...)
        n //= k  # Chia lấy phần nguyên
    return s

# Chạy thử với nhiều test case
for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = convert(n, k)
    ans.reverse()  # Đảo ngược danh sách để đúng thứ tự
    print(''.join(ans))  # Kết hợp các phần tử trong danh sách thành chuỗi

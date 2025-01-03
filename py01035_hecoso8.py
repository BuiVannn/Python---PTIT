def convert(n):
    cnt = 0  # Đếm số bit đã xử lý
    s = ''  # Chuỗi kết quả
    p = 0  # Giá trị tạm thời cho 3 bit

    # Duyệt qua từng bit trong chuỗi (theo thứ tự ngược)
    for i in range(len(n)):
        p += pow(2, cnt) * int(n[i])  # Tính giá trị nhị phân của nhóm 3 bit
        cnt += 1
        if cnt == 3:  # Khi đủ 3 bit
            s += chr(p + ord('0'))  # Chuyển nhóm bit thành ký tự và thêm vào chuỗi
            p = 0  # Reset giá trị p
            cnt = 0  # Reset bộ đếm

    # Xử lý phần dư (nếu số bit không chia hết cho 3)
    if cnt > 0:
        p = 0
        for i in range(cnt):
            p += pow(2, i) * int(n[len(n) - cnt + i])  # Tính giá trị phần dư
        s += chr(p + ord('0'))  # Thêm phần dư vào chuỗi kết quả

    return s

# Test case
n = input()
n = list(n)  # Chuyển chuỗi thành danh sách ký tự
n = n[::-1]  # Đảo ngược chuỗi
ans = (convert(n))  # In kết quả
ans = list(ans)
ans = ans[::-1]
print(''.join(ans))

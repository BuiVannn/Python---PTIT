'''
n = int(input())

dsbai = []
cau = []
for i in range(n):
    a = input()
    cau.append(a)

#print(cau)

i = 0
while i < n:
    so_tu = cau[i].strip().split()
    #print(len(so_tu))
    
    if len(so_tu) == 6 or len(so_tu) == 8:
        dsbai.append(1)
        # Di chuyển đến câu tiếp theo có độ dài khác
        i += 1
        while i < n:
            so_tu = cau[i].strip().split()
            if len(so_tu) != 6 and len(so_tu) != 8:
                break
            i += 1
    elif len(so_tu) == 7:
        dsbai.append(2)
        # Di chuyển đến câu tiếp theo có độ dài khác
        i += 1
        while i < n:
            so_tu = cau[i].strip().split()
            if len(so_tu) != 7:
                break
            i += 1
    else:
        i += 1  # Nếu không phải là 6, 7, hoặc 8 từ, tăng `i` để tránh vòng lặp vô hạn

print(len(dsbai))
for i in dsbai:
    print(i)

'''

n = int(input())

cau = []
for _ in range(n):
    cau.append(input().strip())

dsbai = []  # Danh sách chứa loại của từng bài thơ
i = 0
while i < n:
    # Đếm số từ trong câu thơ hiện tại
    so_tu = cau[i].strip().split()
    len_so_tu = len(so_tu)

    if len_so_tu == 6:  # Khởi đầu của một bài thơ lục bát
        is_luc_bat = True
        while i + 1 < n:
            cau_tiep_theo = cau[i + 1].strip().split()
            len_cau_tiep_theo = len(cau_tiep_theo)
            if len_so_tu == 6 and len_cau_tiep_theo == 8:  # Cặp lục bát (6, 8)
                i += 2
                if i < n:
                    so_tu = cau[i].strip().split()
                    len_so_tu = len(so_tu)
                else:
                    break
            else:
                is_luc_bat = False
                break
        dsbai.append(1)
    elif len_so_tu == 7:  # Có thể là bài thơ thất ngôn tứ tuyệt
        is_that_ngon = True
        for j in range(4):
            if i + j >= n or len(cau[i + j].strip().split()) != 7:
                is_that_ngon = False
                break
        if is_that_ngon:
            dsbai.append(2)
            i += 4
        else:
            i += 1
    else:
        i += 1

print(len(dsbai))
for i in dsbai:
    print(i)
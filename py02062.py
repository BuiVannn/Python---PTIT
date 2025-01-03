'''

def prefix_function(A):
    n = len(A)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and A[i] != A[j]:
            j = pi[j - 1] 
        if A[i] == A[j]:
            j += 1
        pi[i] = j
    return pi

def has_adj_duplicate(A):
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            return True
    return False


def has_square_subarray(A):
    pi = prefix_function(A)
    n = len(A)

    for i in range(n):
        length = i + 1
        border = pi[i]
        period = length - border

        if border > 0 and (length % period == 0) and (2 * period == length):
            return True
    
    return False

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    ok = 1
    if has_adj_duplicate(A):
        ok = 0
        
    if has_square_subarray(A):
        ok = 0
    else: ok = 1
    if ok == 1:
        print("YES")
    else:
        print("NO")

'''

def prefix_function(A):
    """
    Tính mảng pi (prefix function) trong O(n).
    pi[i] là độ dài border (tiền tố = hậu tố) lớn nhất của đoạn A[0..i].
    """
    n = len(A)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and A[i] != A[j]:
            j = pi[j - 1]
        if A[i] == A[j]:
            j += 1
        pi[i] = j
    return pi

def has_adjacent_duplicates(A):
    """
    Kiểm tra xem có cặp phần tử liên tiếp nào trùng nhau không.
    Nếu có, trả về True, ngược lại False.
    """
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            return True
    return False

def has_square_subarray(A):
    pi = prefix_function(A)
    n = len(A)

    for i in range(n):
        length = i + 1   # prefix [0..i] có độ dài = length
        p = pi[i]
        
        # 'Lùi' qua các border (p) nhỏ dần
        while p > 0:
            # period = length - p
            # subSquareLen = 2 * period
            subSquareLen = 2 * (length - p)  # cỡ khối lặp có thể
            if subSquareLen <= length:
                # subSquareLen là độ dài 1 "khối lặp" kết thúc tại i
                # Nếu >= 2 => ta tìm được subarray XX (độ dài >= 2)
                if subSquareLen >= 2:
                    return True
            # Thử border bé hơn
            p = pi[p - 1]

    return False


def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    T = int(input_data[0])
    
    idx = 1
    outputs = []
    
    for _ in range(T):
        N = int(input_data[idx]); idx += 1
        
        # Đọc dãy A
        A = list(map(int, input_data[idx: idx + N]))
        idx += N
        
        # Bước 1: Kiểm tra cặp liền kề trùng
        if has_adjacent_duplicates(A):
            outputs.append("NO")
            continue
        
        # Bước 2: Kiểm tra subarray dạng XX
        if has_square_subarray(A):
            outputs.append("NO")
        else:
            outputs.append("YES")
    
    print("\n".join(outputs))

# Bạn có thể gọi hàm solve() nếu chạy code trực tiếp
# hoặc copy toàn bộ hàm solve() rồi chạy với input chuẩn.
# Ví dụ minh họa (chỉ mang tính kiểm thử nhỏ):

if __name__ == "__main__":
    # Test nhanh bằng cách gán cứng input:
    input_test = """4
7
1 2 3 4 3 4 1
2
1 2
4
1 2 1 2
3
1 2 3
"""
    import io
    import sys

    backup_stdin = sys.stdin
    sys.stdin = io.StringIO(input_test)
    
    solve()  # Chạy hàm solve() với input_test
    
    sys.stdin = backup_stdin

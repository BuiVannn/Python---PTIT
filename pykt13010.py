MOD = 10**9 + 7

def mod_exp(base, exp, mod):
    """Tính base^exp % mod bằng lũy thừa nhanh."""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def sum_of_powers(n, k, mod=MOD):
    """Tính tổng S = 1^k + 2^k + ... + n^k % mod."""
    if n == 0:
        return 0

    total = 0
    current = 1

    while current <= n:
        # Tìm giới hạn của khối
        next_limit = n // (n // current)
        # Số lượng số hạng trong khối
        count = next_limit - current + 1
        # Giá trị tổng của khối
        total = (total + count * mod_exp(current, k, mod)) % mod
        current = next_limit + 1

    return total

# Nhập n và k
n, k = map(int, input("Nhập n và k: ").split())

# Tính tổng
result = sum_of_powers(n, k)
print(result)

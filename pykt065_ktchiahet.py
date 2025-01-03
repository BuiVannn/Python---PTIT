from math import gcd

def sieve_primes(N):
    # Tìm các số nguyên tố từ 2 đến N bằng Sàng Eratosthenes
    is_prime = [True] * (N + 1)
    primes = []
    for p in range(2, N + 1):
        if is_prime[p]:
            primes.append(p)
            for multiple in range(p * p, N + 1, p):
                is_prime[multiple] = False
    return primes

def count_non_divisible(L, R, primes):
    total_numbers = R - L + 1  # Tổng số các số trong đoạn [L, R]
    count = 0  # Số lượng các số chia hết cho ít nhất một số nguyên tố
    n = len(primes)
    for mask in range(1, 1 << n):  # Duyệt tất cả các tập hợp con của primes
        lcm = 1  # Bội số chung nhỏ nhất của các số trong tập hợp con
        bits_set = bin(mask).count('1')  # Số lượng bit 1 trong mask (số phần tử trong tập hợp con)
        for i in range(n):
            if mask & (1 << i):
                p = primes[i]
                # Tính LCM một cách an toàn để tránh tràn số
                lcm = lcm * p // gcd(lcm, p)
                if lcm > R:
                    break  # Không cần xét tiếp nếu LCM lớn hơn R
        else:
            # Nếu không break, tính số lượng số chia hết cho LCM trong đoạn [L, R]
            divisible = R // lcm - (L - 1) // lcm
            if bits_set % 2 == 1:
                count += divisible
            else:
                count -= divisible
    return total_numbers - count

def main():
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            if line == '-1':
                break
            L_R = line.split()
            L, R = map(int, L_R)
            N_line = input().strip()
            while not N_line:
                N_line = input().strip()
            N = int(N_line)
            primes = sieve_primes(N)
            result = count_non_divisible(L, R, primes)
            print(result)
        except EOFError:
            break

if __name__ == '__main__':
    main()

def count_divisors(n):
  """Đếm số ước của một số"""
  count = 0
  for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
      count += 2  # Đếm cả i và n//i
  if int(n**0.5) * int(n**0.5) == n:
    count -= 1  # Trừ đi 1 trường hợp căn bậc hai nếu n là số chính phương
  return count

def find_next_antiprime(x):
  """Tìm số phản nguyên tố bé nhất không nhỏ hơn x"""
  antiprimes = [1]
  max_divisors = 1
  n = 2
  while True:
    divisors = count_divisors(n)
    if divisors > max_divisors:
      antiprimes.append(n)
      max_divisors = divisors
    if n >= x:
      return antiprimes[-1]
    n += 1

# Nhập số lượng test
T = int(input())

# Xử lý từng test
for _ in range(T):
  X = int(input())
  result = find_next_antiprime(X)
  print(result)
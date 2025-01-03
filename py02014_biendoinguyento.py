import bisect


def sieve_of_eratosthenes(limit):    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False 
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
   
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    return primes


primes_up_to_10000 = sieve_of_eratosthenes(100000)
n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    k = bisect.bisect_left(primes_up_to_10000, a[i])
    if k < len(primes_up_to_10000) and primes_up_to_10000[k] == a[i]:
        ans.append(0)
    else:
        if k < len(primes_up_to_10000):
            right_dist = abs(primes_up_to_10000[k] - a[i])  #else float('inf')
        if k > 0:
            left_dist = abs(primes_up_to_10000[k - 1] - a[i])  #else float('inf')
               
        ans.append(min(left_dist, right_dist))

print(max(ans))

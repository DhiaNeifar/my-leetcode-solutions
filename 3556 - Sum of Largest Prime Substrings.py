class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        
        offset = ord("0")
        primes = set()
        for i in range(len(s)):
            curr_n = ord(s[i]) - offset
            if curr_n > 1 and is_prime(curr_n):
                    primes.add(curr_n)
            for j in range(i + 1, len(s)):
                curr_n *= 10
                curr_n += ord(s[j]) - offset
                if curr_n > 1 and is_prime(curr_n):
                    primes.add(curr_n)
        if len(primes) >= 3:
            primes_list = list(primes)
            primes_list.sort()
            return primes_list[-3] + primes_list[-2] + primes_list[-1]
        return sum(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
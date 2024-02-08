class Solution:
    def countPrimes(self, n: int) -> int:

        # If there are no primes at all
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = 0

        # Use sieve of Eratosthenes
        for num in range(2, int(n ** 0.5) + 1):
            if is_prime[num]:
                for multiple in range(num * num, n, num):
                    is_prime[multiple] = False
        return sum(is_prime)

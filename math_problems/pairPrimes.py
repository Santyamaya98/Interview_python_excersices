# User function Template for python3

class Solution:
    def prime_pairs(self, n):

        def isPrime(num):
            if num in (1, 2, 3):
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i < num:
                if num % i == 0 or num % (i + 2):
                    return False
                i += 6
            return True

        primePairs = set()
        primes = []
        for i in range(3, n + 1, 2):
            if isPrime(i) == True:
                primes.append(i)

        primePairs.add((primes[0], primes[0]))

        for i, num in enumerate(primes):
            if i < len(primes) and i + 1 < len(primes):
                primePairs.add(primes[i], primes[i + 1])

        result = " ".join(str(primePairs))
        return result

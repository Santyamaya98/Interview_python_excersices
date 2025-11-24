class Solution:
    def isPrime(self, n):
        """Return True if n is prime else False"""
        if n == 1:
            return False
        if n%2 == 0:
            return False
        i = 3
        while i < n:
            if n%i == 0:
                return False
            i += 2 
        return True
                

print(Solution.isPrime(None, 43))
class Solution:
    def prime_Sum(self, n):
        def isPrime(num):
            if num < 2:
                return False
            if num in (2, 3):
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i < num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        if n == 1:
            return 1
        if n == 2:
            return 2
        if n <= 4:
            return 5

        suma = 2  # start with prime number 2
        for i in range(3, n + 1, 2):
            if isPrime(i):
                suma += i

        return suma

class Solution:
    def sieve(self, n):
        def isPrime(num):
            if num < 2:
                return False
            if num == 2:
                return True
            if num == 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True   
            
        primes = [i for i in range(2,(n+1)) if isPrime(i)!=False ]

        return primes
            
    def sieve(self, n):
        if n < 2:
            return []
        
        # Crear lista de primos potenciales
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 y 1 no son primos

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Marcar múltiplos de i desde i*i
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        # Devolver lista de primos
        return [i for i in range(2, n + 1) if is_prime[i]]   
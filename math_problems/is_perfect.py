class Solution:
    def isPerfect(self, n: int) -> bool:
        # A perfect number must be a positive integer.
        # The smallest perfect number is 6.
        if n <= 1:
            return False

        # Initialize the sum of proper divisors. 
        # Start with 1, as 1 is a proper divisor of every number > 1.
        sum_of_divisors = 1 
        
        # Iterate from 2 up to the square root of n (inclusive).
        # We only need to check up to the square root for divisors.
        i = 2
        while i * i <= n:
            if n % i == 0:
                # If i divides n, then i is a divisor.
                sum_of_divisors += i
                
                # Also, n/i is a divisor (the 'pair').
                # We only add n/i if it is NOT the same as i.
                # If i * i == n, then i and n/i are the same (i.e., i is the square root of n).
                # Since we already added 'i', we shouldn't add it again.
                if i * i != n:
                    sum_of_divisors += (n // i)
            
            i += 1
            
        # A number is perfect if the sum of its proper divisors equals the number itself.
        return sum_of_divisors == n
        

ob = Solution.isPerfect(None, 12)
print(ob)
ob = Solution.isPerfect(None, 8128)
print(ob)
ob = Solution.isPerfect(None, 6)
print(ob)
ob = Solution.isPerfect(None, 10)
print(ob)
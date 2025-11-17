class Solution:
    @staticmethod
    def last_prime(n):
        """
        Finds the largest prime factor of a given integer n using trial division.
        """
        # Ensure n is a positive integer
        n = abs(int(n))
        
        # 1. Handle edge case for n <= 1
        if n <= 1:
            return 1 # Or raise an error, depending on requirements

        largest_prime = 1 # Initialize the largest prime found

        # 2. Divide by 2
        # Handle 2 separately to simplify the loop for odd numbers (divisors >= 3).
        if n % 2 == 0:
            largest_prime = 2
            while n % 2 == 0:
                n //= 2
        
        # 3. Divide by odd numbers starting from 3 up to sqrt(n)
        # We only need to check factors up to the square root of n.
        # i starts at 3 and increments by 2 (checking only odd numbers).
        i = 3
        while i * i <= n:
            if n % i == 0:
                # i is a prime factor
                largest_prime = i
                # Keep dividing n by this factor until it's no longer divisible
                while n % i == 0:
                    n //= i
            i += 2
            
        # 4. Handle the remaining factor
        # If n is still greater than 1 after the loop, the remaining n itself 
        # must be a prime factor (and it must be the largest one).
        if n > 1:
            largest_prime = n
            
        return largest_prime

# --- Example Usage (Called correctly on the class instance or statically) ---
# Call the method directly on the class since it is a @staticmethod
print(f"Largest prime factor of 5: {Solution.last_prime(5)}")         # Output: 5
print(f"Largest prime factor of 13195: {Solution.last_prime(13195)}") # Output: 29
print(f"Largest prime factor of 973: {Solution.last_prime(973)}")     # 973 = 7 * 139 (Output: 139)
print(f"Largest prime factor of 55: {Solution.last_prime(55)}")       # Output: 11
print(f"Largest prime factor of 24: {Solution.last_prime(24)}")       # Output: 3
import functools
import math # Added math import for the corrected nCr method

class Solution:
    # This method is highly inefficient and uses complex custom factorial logic.
    # The lru_cache is ineffective here as there are no overlapping subproblems 
    # in the factorial calculation. It's kept for structural adherence.
    @functools.lru_cache(maxsize=None)
    def nCr(self, n, r):
        """ C(n,r) = n! / r! * (n-r) !"""
        # Base cases
        if r < 0 or r > n:
            return 0
        if r == 0 or r == n:
            return 1
        
        # Use the standard, correct, and efficient math.factorial approach
        # which avoids the complex and error-prone custom factorial logic.
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    
    @functools.lru_cache(maxsize=None)
    def nCr_ia(self, n, r):
        """
        Calculates the binomial coefficient C(n,r) using 
        Pascal's Identity with memoization.
        """
        # Ensure n and r are treated as integers
        n, r = int(n), int(r) 

        # 2. Base Cases (Stopping the recursion)
        if r < 0 or r > n:
            return 0
        if r == 0 or r == n:
            return 1
        if r == 1 or r == n - 1:
            return n

        # 3. Recursive Step (Pascal's Identity)
        # This works correctly due to lru_cache memoization.
        return self.nCr_ia(n - 1, r - 1) + self.nCr_ia(n - 1, r)
    
    def nCr_memo(self, n, r, memo=None):
        """
        Calculates C(n,r) using Pascal's Identity and manual memoization.
        """
        if memo is None:
            memo = {} # Initialize the cache on the first call
        
        # 1. Check the Cache (Tuple (n, r) is used as the key)
        if (n, r) in memo:
            return memo[(n, r)]

        # Base Cases
        if r < 0 or r > n:
            return 0
        if r == 0 or r == n:
            return 1

        # Recursive Step
        result = self.nCr_memo(n - 1, r - 1, memo) + self.nCr_memo(n - 1, r, memo)
        
        # 2. Store the Result in the Cache
        memo[(n, r)] = result
        
        return result
        
        
if __name__=="__main__":
    # 1. CREATE an instance of the class.
    solver = Solution()
    
    # 2. CALL the methods on the instance (solver).

    # nCr calls (using the factorial method)
    ob1 = solver.nCr(31, 22)
    print(ob1)
    ob2 = solver.nCr(11, 2)
    print(ob2)
    ob3 = solver.nCr(89, 70)
    print(ob3)

    # nCr_ia calls (using the recursive Pascal's Identity method)
    ob4 = solver.nCr_ia(31, 22)
    print(ob4)
    ob5 = solver.nCr_ia(11, 2)
    print(ob5)
    ob6 = solver.nCr_ia(89, 70)
    print(ob6)
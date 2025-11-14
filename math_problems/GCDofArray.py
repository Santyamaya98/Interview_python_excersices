class Solution:
    def gcd(self, n, arr):

        n = int(n)
        arr = list(arr)
        if len(arr)==1:
            return arr[0]
        GCD = []
        for i in range(n-1):
            a = arr[i]
            b = arr[i+1]

            while b != 0:
                a,b = b, a%b
                GCD.append(abs(a))

            if i+1 == n:
                break
        return min(GCD)
    @staticmethod
    # The function now accepts 'n' (the length) and 'arr' (the array).
    def gcd_ia(self, n, arr):
        
        # We can cast n to int if we trust the caller to pass the correct length,
        # but the safest approach is to use len(arr) for the actual loop bounds.
        # We will use the provided n to check array length, assuming it's correct.
        
        def find_gcd_of_two(a, b):
            """Calculates the Greatest Common Divisor of two numbers using the Euclidean Algorithm."""
            # Ensure numbers are non-negative and integer
            a, b = abs(int(a)), abs(int(b)) 
            while b:
                a, b = b, a % b
            return a

        # Handle edge cases using the provided length 'n' or the array itself.
        # If n is 0, the array is empty.
        if n == 0 or not arr:
            return 0 
        
        # If n is 1, the GCD is the only element.
        if n == 1:
            return arr[0]
        
        # 4. Initialize the running GCD
        # Start the result with the first element.
        result_gcd = arr[0]

        # 5. Iterate through the remaining elements (from the second element up to n-1)
        # Using n for the loop range ensures we respect the input count.
        for i in range(1, n):
            # Check if the array actually has the element at index i (for safety)
            if i < len(arr):
                current_num = arr[i]
                
                # Update the result: new_gcd = GCD(old_gcd, current_num)
                result_gcd = find_gcd_of_two(result_gcd, current_num)
        
        return result_gcd

print(Solution.gcd(None, 3, [2,4,6]))
print(Solution.gcd(None, 1, [15]))
print(Solution.gcd(None, 4, [9,6,33,42]))
print(Solution.gcd_ia(None, 4, [35, 40, 45, 3]))


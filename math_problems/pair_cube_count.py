class Solution:
    @staticmethod
    def pairCubeCount(n):
        count = 0
        # a starts from 1, and a^3 <= n
        a = 1
        while a * a * a <= n:
            remainder = n - a * a * a
            # Find cube root of remainder
            b = round(remainder ** (1/3))
            print(b)
            # Check if b^3 equals the remainder and b >= 0
            if b * b * b == remainder and b >= 0:
                count += 1
            a += 1
        return count   
            

sol = Solution.pairCubeCount(9)
print(sol)
sol = Solution.pairCubeCount(16)
print(sol)
sol = Solution.pairCubeCount(27)
print(sol)
sol = Solution.pairCubeCount(5002)
print(sol)
sol = Solution.pairCubeCount(1729)
print(sol)

class Solution:
    @staticmethod
    def isPower(x,y):
        if y == 1:
            return True
        """
        Given two positive integers x and y, 
        determine if y is a power of x. If y is a power of x,
        return True. Otherwise, return False.
        b^x = n -> log(b, n) = x
        """
        for i in range(0,y):
            result = x**i
            if result == y:
                return True
            
        return False
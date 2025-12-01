#User function Template for python3

class Solution:
    @staticmethod
    def countSquares(n):
        """
        Given a positive integer n, find the number of perfect squares that are less than n
        in the sample space of perfect squares. The sample space consists of all perfect 
        squares starting from 1 (i.e., 1, 4, 9, 16, 25, …)
        """
        count = 0
        perfect_square = 0
        for i in range(1, n+1):
            perfect_square = i ** 2
            if perfect_square < n:
                count +=1
            else:
                break
        return count

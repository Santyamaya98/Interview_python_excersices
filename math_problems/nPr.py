class Solution:
    def nPr(self, n, r):
        "5!/(5-2)! = 5!/3!"
        n = int(n)
        r = int(r)
        if n <= 2:
            return n
        def factorial(n, result):
            new_result = result*(n-1)
            n -= 1 
            if n == 1 :
                return new_result
            else:
                return factorial(n, new_result)
        
        if n <= 3:
            N = n*(n-1) 
        else:
            result_n = n * (n-1)
            N = factorial(n-1, result_n)
        r = abs(n-r)
        if r == 0 or r == 1:
            return N
        if r <= 3:
            R = r * (r-1)
        else:                    
            result_r = r * (r-1)
            R = factorial((abs(r)-1),result_r)

        return int(N/R)
    
if __name__=="__main__":
    ob = Solution.nPr(None, 7, 6)
    print(ob)
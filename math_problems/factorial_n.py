class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        "n! = (n * n-1 * n-2 ... 2 * 1)"
        n = int(n)
        if n == 0 or n==1:
            return 1
        if n >= 4:
            result = n * (n-1)
            n -= 1 
            def recursive(n, result):
                new_result = result * (n-1)
                n-=1
                if n == 1:
                    return new_result
                else:
                    return recursive(n,new_result)
            new_result = recursive(n, result)
            return new_result
        
        result = n * (n-1)
        n -= 1 

        return result

    
if __name__=="__main__":
    ob = Solution.factorial(None, 0)
    print(ob)
    ob = Solution.factorial(None, 1)
    print(ob)
    ob = Solution.factorial(None, 3)
    print(ob)
    ob = Solution.factorial(None, 4)
    print(ob)
    ob = Solution.factorial(None, 5)
    print(ob)
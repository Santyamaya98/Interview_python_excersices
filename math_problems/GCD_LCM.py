
class Solution:
    def lcmAndGcd(self, a, b):
        """Return the minimun commun multiple of two numbers"""

            
        a, b, = int(a), int(b)
        result = {}
        for i in range(1, max(a,b)):
            result[f'{i}_{a}'] = a*i
            if a*i % b == 0:
            # Found the first common multiple
                mcm = a*i
                break
            else: 
                if b*i % a == 0:
                    mcm = b*i
                    break

        while b != 0:

            a, b = b, a % b
        gcd = abs(a)
        return mcm, gcd
            
 
        




            
             
            


if __name__ == "__main__":
    a = input('type two integer to find GCD -->  ')
    b = input('type two integer to find GCD -->  ')
    ob = Solution.lcmAndGcd(None, a, b)
    print(ob)

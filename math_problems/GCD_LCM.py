
class Solution:
    def gcd(self, a, b):
        """Return the greatest common divisor (GCD) of a and b"""
        a, b = int(a), int(b)
        while b != 0:
            print('a,b =', a,b)
            print('a mod b', a%b)
            a, b = b, a % b
        return abs(a)

            
             
            


if __name__ == "__main__":
    a = input('type two integer to find GCD -->  ')
    b = input('type two integer to find GCD -->  ')
    ob = Solution.gcd(None, a, b) 
    print(ob)
    import math
    print('********'*10)
    print(math.gcd(int(a), int(b)))
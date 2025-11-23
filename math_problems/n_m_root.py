class Solution:
    def nthRoot(self, n, m):
       # code here
       """You are given 2 numbers n and m, the task is to find n√m
       (nth root of m). If the root is not integer then return -1.
       Input: n = 3, m = 8
       Output: 2   
       Explanation: 23 = 8
       """
       if n >0:
           n = 1/n
    
       root = m**n
       print(root)
       str_root = str(m**n)
       for i, char in enumerate(str_root):
           if str_root[i] ==".":
                if int(str_root[i+1]) > 0:
                    return -1
                try:
                    if int(str_root[i+2]) > 0 :
                        return -1
                except:
                    pass
                return int(root)
                    
print(Solution.nthRoot(None, 4,16))
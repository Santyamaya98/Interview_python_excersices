class Solution:
    @staticmethod
    def isSquare(x1,y1,x2,y2,x3,y3,x4,y4):
        """check if the point can form a square"""
        if x1 == x2 and x3 == x4 and y1 == y2 and y3 == y4:
            return "No"
        
        
        h = (x1 + x2), (x3+x4)
        l = (y1 + y2), (y3+y4)

        #print(f'h: {h}, l: {l}')

        differenceh = (x1 + x2) - (x3+x4)
        differencel = (y1 + y2) - (y3+y4)

        #print(f'dh: {differenceh}, dl: {differencel}')

        diagh = ((x1+x3)**2 + (y1+y3) **2)**0.5
        diagl = ((x2+x4)**2 + (y2+y4) **2)**0.5

        #print(f'diagh: {diagh}, diagl {diagl}')
        return "Yes" if h == l or diagh==diagl else "No"


print(Solution.isSquare(2,1, 10,20, 5,6, 10,10))


print(Solution.isSquare(-1, -1, 5, -1, 5, 5, -1, 5,))

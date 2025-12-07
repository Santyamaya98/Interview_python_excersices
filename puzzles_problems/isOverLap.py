#User function Template for python3

class Solution:
    @staticmethod
    def doOverlap(L1, R1, L2, R2):
        #code here
        """
        Given two rectangles, find if the given two rectangles overlap or
        not. A rectangle is denoted by providing the x and y coordinates
        of two points: the left top corner and the right bottom corner 
        of the rectangle. Two rectangles sharing a side are considered
        overlapping. (L1 and R1 are the extreme points of the first 
        rectangle and L2 and R2 are the extreme points of the second 
        rectangle).

        Note: It may be assumed that the rectangles are parallel to the coordinate axis.
        """

        check= set((L1, R1, L2, R2))
        if len(check) < 4:
            return 0
        points = {"1":L1, "2":R1, "3":L2, "4":R2}
        def extractValues(dict, key1, key2):
            return dict[key1][0], dict[key1][1], dict[key2][0], dict[key2][1]
        x1, y1, x2, y2 = extractValues(points, "1", "2")
        x3, y3, x4, y4 = extractValues(points, "3", "4")

        if x2 < x3 or x4 < x1:
            return 0

        # If one rectangle is above other
        if y1 < y4 or y3 < y2:
            return 0
        
        
        return 1 
    
L1,R1,L2,R2 = (-91, 100), (-64, -39), (63, -71), (89, -74)
print(Solution.doOverlap(L1,R1,L2,R2))
L1,R1,L2,R2 = (84, 17), (91, -30), (-73, -65), (-66, -98)
print(Solution.doOverlap(L1,R1,L2,R2))
L1,R1,L2,R2  = (53, -45), (64, -49), (-85, -12), (-30, -94)
print(Solution.doOverlap(L1,R1,L2,R2))
L1,R1,L2,R2  = (-49, -33), (36, -80), (9, 21), (83, -53)
print(Solution.doOverlap(L1,R1,L2,R2))
L1,R1,L2,R2  = (-47, -99), (-15, -99), (-56, 94), (-8, -47)
print(Solution.doOverlap(L1,R1,L2,R2))
L1,R1,L2,R2  = (-4, 23), (4, 22), (63, 44), (71, -92)
print(Solution.doOverlap(L1,R1,L2,R2))
L1,R1,L2,R2  = (15, -29), (41, -87), (83, 6), (86, -8)
print(Solution.doOverlap(L1,R1,L2,R2))

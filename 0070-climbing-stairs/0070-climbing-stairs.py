class Solution(object):
    def climbStairs(self, n):
        a, b, c = 0, 1, 0
        
        for i in range(n):
            c = a + b
            a, b = b, c
        
        return b
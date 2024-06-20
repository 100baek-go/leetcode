class Solution(object):
    def plusOne(self, digits):
        New=[]
        n=0
        for i in range(len(digits)):
            n=(n*10)+digits[i]
        N=str(n+1)
        for j in N:
            New.append(int(j))
        return New
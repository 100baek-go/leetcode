class Solution:
    def judgeCircle(self, moves: str) -> bool:
        def move(a,i,j):
            if(a=='L'):
                j-=1
            elif(a=='R'):
                j+=1
            elif(a=='U'):
                i-=1
            else:
                i+=1
            return i,j
        i=j=0
        for a in moves:
            i,j=move(a,i,j)
        return i==0 and j==0
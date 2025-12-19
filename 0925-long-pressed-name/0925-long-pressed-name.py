class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j=0,0
        c1,c2=1,1
        n,t=len(name),len(typed)
        
        if t<n or typed[0]!= name[0] or typed[t-1]!=name[n-1] or set(typed)!=set(name):
            return False

        while j < t:
            if i<n and typed[j]!=name[i]:
                return False
            if i==n and typed[j]!=name[i-1]:
                return False

            while i+1 < n and name[i]==name[i+1]:
                c1+=1
                i+=1
            while j+1 < t and typed[j]==typed[j+1]:
                c2+=1
                j+=1
            if c2< c1:
                return False

            c1,c2=1,1

            if i<n:
                i+=1
            j+=1

        return True
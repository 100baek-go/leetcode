class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre= 0
        count= 1
        actual= 0

        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                count+=1

            else:
                actual+= min(pre,count)
                pre= count
                count= 1

        actual+= min(pre,count)

        return actual
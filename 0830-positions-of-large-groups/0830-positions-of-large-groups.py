class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        word = ''
        leng = len(s)
        num = 0
        count = 1

        for i in range(leng):
            if s[i] != word:
                if count > 2:
                    res.append([num, i-1])
                word = s[i]
                num = i
                count = 1
            else:
                count += 1
          
        if count != 1 and count > 2:
            res.append([num, leng-1])

        return res
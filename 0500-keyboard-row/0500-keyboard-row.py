class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l =  list("qwertyuiop")
        l1 =  list("asdfghjkl")
        l2 =  list("zxcvbnm")
        k = []
        o,p,q = 0,0,0
        for i in words:
            m,n,x = i,i,i
            for j in m:
                if j.lower()  in l:
                    o += 1
                else:
                    break
                    
            if o == len(i):
                k.append(i)
            o = 0
            for a in n:
                if a.lower() in l1:
                   
                    p += 1
                   
                else:
                    break
                    
            if p == len(i):
                k.append(i)
            p = 0
            for b in x:
                if b.lower() in l2:
                    q += 1
                else:
                    break
                    
            if q == len(i):
                k.append(i)
            q = 0
        return k
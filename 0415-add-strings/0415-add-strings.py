class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2)>len(num1):
            num1='0'*(len(num2)-len(num1))+num1
        if len(num1)>len(num2):
            num2='0'*(len(num1)-len(num2))+num2
        ans=''
        carry=0
        for i in range(len(num1)-1,-1,-1):
            t=int(num1[i])+int(num2[i])+carry
            carry=0
            if t<10:
                ans+=str(t)
            else:
                t=str(t)
                ans+=t[1]
                carry=int(t[0])
        if carry>0:
            ans+=str(carry)
        return ans[::-1]
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res=[]
        hashmap={0:[],1:[]}
        for num in nums:
            if num%2:
                hashmap[1].append(num)
            else:
                hashmap[0].append(num)
        for i in range(len(nums)):
            if i%2:
                res.append(hashmap[1].pop())
            else:
                res.append(hashmap[0].pop())
        return res
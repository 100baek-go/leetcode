class Solution(object):
    def removeElement(self, nums, val):
        l=len(nums)
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i+=1
        k=len(nums)
        while len(nums)<l:
            nums.append('_')
        return k
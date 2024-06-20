class Solution(object):
    def removeDuplicates(self, nums):
        l=len(nums)
        i=1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i+=1
        k=len(nums)
        while len(nums)<l:
            nums.append('_')
        return k
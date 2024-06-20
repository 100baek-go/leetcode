class Solution(object):
    def searchInsert(self, nums, target):
        i=0
        j=0
        while i<len(nums):
            if nums[i]==target:
                return i
            else:
                i+=1
        if target<nums[0]:
            return 0
        elif target>nums[len(nums)-1]:
            return len(nums)
        else:
            while j<len(nums)-1:
                if target>=nums[j] and target<=nums[j+1]:
                    return j+1
                else:
                    j+=1
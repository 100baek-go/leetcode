class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return 0 if max(nums)-min(nums)-2*k<=0 else max(nums)-min(nums)-2*k
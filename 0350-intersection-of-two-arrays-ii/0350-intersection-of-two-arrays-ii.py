class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        for number in nums1:
            table[number] = table.get(number, 0) + 1
       
        res = []
        for num in nums2:
            if num in table:
                if table[num] > 0:
                    res.append(num)
                    table[num] = table[num] - 1
        return res
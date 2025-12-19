class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alsum = sum(aliceSizes)
        bobsum = sum(bobSizes)
        k = (alsum + bobsum)//2

        for i in aliceSizes:
            num = k - (alsum - i)
            if num in bobSizes:
                res = [i, num]
                return res
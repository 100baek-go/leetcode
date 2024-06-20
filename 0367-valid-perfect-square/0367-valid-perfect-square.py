class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return sqrt(num) == floor(sqrt(num))
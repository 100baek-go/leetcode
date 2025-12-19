class Solution:
    def binaryGap(self, n: int) -> int:
        maxDistance = 0
        curr, prev = 0, 0
        binary = bin(n)[2:]
        while curr != len(binary):
            if binary[curr] == '1':
                maxDistance = max(maxDistance, curr-prev)
                prev = curr
            curr += 1
        return maxDistance
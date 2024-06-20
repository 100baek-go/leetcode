class Solution(object):
    def titleToNumber(self, columnTitle):
        s = columnTitle[::-1]
        return sum([(ord(s[i]) - 64) * (26 ** i) for i in range(len(s))])
        
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        chars = re.findall(r'[a-z]', licensePlate)
        m = {}
        for char in chars:
            m[char] = m.get(char, 0) + 1
        words = sorted(words, key=lambda x: len(x))
        for word in words:
            m_cp = m.copy()
            for c in word:
                if c in m_cp:
                    m_cp[c] = m_cp[c] - 1
            if all(m_cp[key] <= 0 for key in m_cp):
                return word
        return
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            freq[t[i]] = freq.get(t[i], 0) - 1
        freq[t[-1]] = freq.get(t[-1], 0) - 1
        for element in freq:
            if freq[element]:
                return element
        return ""
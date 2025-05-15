class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = {}
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1
        
        right, left = 0, 0
        result = 0
        s2_freq = {}

        while right < len(s2):
            s2_freq[s2[right]] = s2_freq.get(s2[right], 0) + 1
            
            while s2_freq[s2[right]] > s1_freq.get(s2[right], 0):
                s2_freq[s2[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
            right += 1
        
        return result >= len(s1)
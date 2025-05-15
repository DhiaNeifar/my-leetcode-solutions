class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right, left = 0, 0
        freq = {}
        result = 0
        
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
            
            right += 1
        
        return result
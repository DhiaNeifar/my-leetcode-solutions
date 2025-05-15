class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        result = 0
        frequency = {}
        while right < len(s):
            frequency[s[right]] = frequency.get(s[right], 0) + 1

            while frequency[s[right]] > 1:
                frequency[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)

            right += 1
        return result
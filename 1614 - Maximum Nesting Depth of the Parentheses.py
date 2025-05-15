class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_ = 0
        for char in s:
            if char == '(':
                count += 1
            if char == ')':
                max_ = max(count, max_)
                count -= 1
        return max_
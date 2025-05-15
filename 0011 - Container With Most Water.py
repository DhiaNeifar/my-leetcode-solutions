class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            if height[0] < height[1]:
                return height[0]
            return height[1]
    
        i, j, maximum = 0, len(height) - 1, 0
        while i != j:
            x = -1
            if height[i] < height[j]:
                x = height[i]
                i += 1
            else:
                x = height[j]
                j -= 1
            new = x * (j - i + 1)
            if maximum < new:
                maximum = new
        return maximum
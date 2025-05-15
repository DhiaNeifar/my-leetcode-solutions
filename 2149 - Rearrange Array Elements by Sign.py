class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = [], []
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        i = 0
        results = []
        while i < len(positive):
            results.append(positive[i])
            results.append(negative[i])
            i += 1
        return results
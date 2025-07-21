class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        freq = {-1: [], 1: []}
        for index, num in enumerate(nums):
            freq[num].append(index)

        if len(freq[-1]) % 2 == 1 and len(freq[1]) % 2 == 1:
            return False
        result = []
        for key in freq:
            l = freq[key]
            m = 0
            if len(l) % 2 == 0:
                for i in range(0, len(l), 2):
                    m += l[i + 1] - l[i] - 1
                m += len(l) // 2
                result.append(m)
        return min(result) <= k
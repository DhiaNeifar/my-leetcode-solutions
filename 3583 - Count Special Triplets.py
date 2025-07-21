from collections import defaultdict
import bisect

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        index = defaultdict(list)
        for ind, num in enumerate(nums):
            index[num].append(ind)
        
        result = 0
        const = 10 ** 9 + 7
        for element in index:
            if element != 0:
                if element * 2 in index:
                    l1 = index[element]
                    l2 = index[element * 2]
                    for j in l1:
                        if l2[0] < j < l2[-1]:
                            ind = bisect_left(l2, j)
                            result += ind * (len(l2) - ind)
                            result %= const
            else:
                l1 = index[element]
                n = len(l1)
                result += n * (n - 1) * (n - 2) // 6
                result %= const
                    
        return result
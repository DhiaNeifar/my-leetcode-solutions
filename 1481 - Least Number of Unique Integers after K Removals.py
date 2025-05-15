class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequencies = {}
        for number in arr:
            frequencies[number] = frequencies.get(number, 0) + 1
        frequencies = sorted(frequencies.values())
        i = 0
        count = 0
        while i < len(frequencies) and count + frequencies[i] <= k:
            count += frequencies[i]
            i += 1
        return len(frequencies) - i
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        frequencies = list(freq.values())
        frequencies.sort()
        
        result = inf
        for i in range(len(frequencies)):
            to_delete = 0
            for j in range(len(frequencies)):
                to_delete += frequencies[j] if frequencies[j] < frequencies[i] else max(0, frequencies[j] - (frequencies[i] + k))
            result = min(result, to_delete)
        
        return result
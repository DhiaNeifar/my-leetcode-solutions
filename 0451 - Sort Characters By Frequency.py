class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = {}
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        split = [char for char in s]
        split.sort()
        return "".join(sorted(split, key=lambda char: frequency[char], reverse=True))
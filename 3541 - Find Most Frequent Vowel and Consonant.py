class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels_count = [0] * 26
        consonants_count = [0] * 26

        const = ord('a')
        for char in s:
            index = ord(char) - const
            if char in vowels:
                vowels_count[index] += 1
            else:
                consonants_count[index] += 1

        return max(vowels_count) + max(consonants_count)
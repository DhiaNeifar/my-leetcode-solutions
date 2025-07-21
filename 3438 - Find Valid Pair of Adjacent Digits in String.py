class Solution:
    def findValidPair(self, s: str) -> str:
        pairs = []
        const = ord('0')
        table = [0 for _ in range(10)]
        index = ord(s[0]) - const
        table[index] += 1
        for i in range(1, len(s)):
            index = ord(s[i]) - const
            table[index] += 1
            if s[i] != s[i - 1]:
                pairs.append(s[i - 1] + s[i])
        
        for pair in pairs:
            first_char, second_char = pair[0], pair[1]
            first_index, second_index = ord(first_char) - const, ord(second_char) - const
            if table[first_index] == first_index and table[second_index] == second_index:
                return pair
        
        return ""
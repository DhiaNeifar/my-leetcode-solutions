class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i, j, k, l = 0, 0, 0, 0
        while i < len(word1) and j < len(word2) and word1[i][k] == word2[j][l]:
            k += 1
            l += 1
            if k == len(word1[i]):
                i += 1
                k = 0
            if l == len(word2[j]):
                j += 1
                l = 0
        if i == len(word1) and j == len(word2):
            return True
        return False
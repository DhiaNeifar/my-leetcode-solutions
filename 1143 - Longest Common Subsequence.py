class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        result = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for row, char1 in enumerate(text1, 1):
            for column, char2 in enumerate(text2, 1):
                result[row][column] = max(result[row - 1][column], result[row][column - 1])
                if char1 == char2:
                    result[row][column] = result[row - 1][column - 1] + 1
        return result[-1][-1]
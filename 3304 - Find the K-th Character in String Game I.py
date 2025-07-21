class Solution:
    def kthCharacter(self, k: int) -> str:
        result = [0]
        while len(result) < k:
            n = len(result)
            for index in range(n):
                result.append((result[index] + 1) % 26)
        return chr(result[k - 1] + ord('a'))
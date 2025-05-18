class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        max_len = max([len(word) for word in words])
        if len(words) != max_len:
            return False
        words = [word + '0' * (max_len - len(word)) for word in words]
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i][j] != words[j][i]:
                    return False
        return True
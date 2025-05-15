class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        for word in words:
            new_word = word.lower()
            for row in rows:
                if new_word[0] in row:
                    if CheckRow(new_word, row):
                        result.append(word)
        return result


def CheckRow(word, row):
    for char in word:
        if char not in row:
            return False
    return True
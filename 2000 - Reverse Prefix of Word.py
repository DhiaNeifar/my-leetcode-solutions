class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for index, letter in enumerate(word):
            if letter == ch:
                return word[:index + 1][::-1] + word[index + 1:]
        return word
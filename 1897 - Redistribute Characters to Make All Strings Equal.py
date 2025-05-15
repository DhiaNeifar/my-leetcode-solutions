class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        _dict = {}
        for word in words:
            for char in word:
                if char in _dict:
                    _dict[char] += 1
                else:
                    _dict[char] = 1
        for value in _dict.values():
            if value % len(words):
                return False
        return True
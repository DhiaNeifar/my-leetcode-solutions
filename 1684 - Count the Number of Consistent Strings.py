class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0
        for word in words:
            v = True
            for char in word:
                if char not in allowed:
                    v = False
                    break
            if v:
                consistent += 1
        return consistent
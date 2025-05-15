class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        l = [False for i in range(len(s) + 1)]
        l[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                len_word = len(word)
                if i + len_word <= length and word == s[i: i + len_word]:
                    l[i] = l[i + len_word]
                if l[i]:
                    break
        
        return l[0]
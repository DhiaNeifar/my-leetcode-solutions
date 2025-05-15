class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        PatternDict = {}
        DictPattern = {}
        if len(words) != len(pattern):
            return False
        for (index, word) in enumerate(words):
            WordSaved1 = PatternDict.get(pattern[index], "")
            WordSaved2 = DictPattern.get(word, "")
            if WordSaved1 == "" and WordSaved2 == "":
                PatternDict[pattern[index]] = word
                DictPattern[word] = pattern[index]
            else:
                if WordSaved1 != word or WordSaved2 != pattern[index]:
                    return False
        return True
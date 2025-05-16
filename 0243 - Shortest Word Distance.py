class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_index = -1
        word2_index = -1
        result = len(wordsDict)
        for index, word in enumerate(wordsDict):
            if word == word1:
                word1_index = index
            if word == word2:
                word2_index = index
            if word1_index != -1 and word2_index != -1: 
                result = min(result, abs(word2_index - word1_index)) 
        return result
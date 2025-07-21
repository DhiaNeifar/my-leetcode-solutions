class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        filtered = []
        for response in responses:
            filtered.extend(set(response))
        freq = {}
        ma = 0
        for word in filtered:
            freq[word] = freq.get(word, 0) + 1
            ma = max(ma, freq[word])
        words = [key for key, value in freq.items() if value == ma]
        words.sort()
        print(words)
        return words[0]
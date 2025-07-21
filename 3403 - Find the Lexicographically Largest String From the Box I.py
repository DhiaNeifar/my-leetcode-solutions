class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        const = ord('a')
        starting_index_tracker = [[] for _ in range(26)]

        for index, char in enumerate(word):
            starting_index_tracker[ord(char) - const].append(index)

        result = set()
        for i in range(25, -1 ,-1):
            if starting_index_tracker[i]:
                break
        
        result = set()

        for starting_index in starting_index_tracker[i]:
            result.add(word[starting_index: min(len(word), starting_index + len(word) - numFriends + 1)])
            
        result = sorted(list(result))

        return result[-1]
class Solution:
    def reverseWords(self, s: str) -> str:
        word = ''
        words = []
        for element in s:
            if element == ' ':
                if word != '':
                    words.insert(0, word)
                    word = ''
            else:
                word += element
        if word != '':
            words.insert(0, word)
        return ' '.join(u for u in words)
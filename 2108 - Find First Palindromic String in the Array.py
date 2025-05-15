class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(string):
            i = 0
            j = len(string) - 1
            while i < j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True
        index = 0
        while index < len(words):
            if is_palindrome(words[index]):
                return words[index]
            index += 1
        return ''
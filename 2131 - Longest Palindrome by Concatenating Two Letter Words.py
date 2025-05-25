class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        palindromes = Counter()
        non_palindromes = Counter()

        for word in words:
            if word[0] == word[1]:
                palindromes[word] += 1
            else:
                non_palindromes[word] += 1

        result = 0
        center = False

        # Count pairs for palindromes
        for pal, count in palindromes.items():
            pairs = count // 2
            result += pairs * 4   # Each pair contributes 4 (2+2)
            if count % 2 == 1:
                center = True     # One odd palindrome can go in the center

        # Count pairs for non-palindromes
        for word in non_palindromes:
            rev = word[::-1]
            if rev in non_palindromes:
                pairs = min(non_palindromes[word], non_palindromes[rev])
                result += pairs * 4
                non_palindromes[word] = 0
                non_palindromes[rev] = 0

        if center:
            result += 2  # You can put one odd palindrome pair in the center

        return result
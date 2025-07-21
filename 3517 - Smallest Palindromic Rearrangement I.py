class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0 for _ in range(26)]
        const = ord('a')
        for char in s:
            index = ord(char) - const
            freq[index] += 1
        
        result = []
        special = None
        for i in range(26):
            div, rest = divmod(freq[i], 2)
            char = chr(i + const)
            if rest:
                special = char
            if div:
                result.append(char * div)
        
        inverse = result[::-1]

        if special is not None:
            result.append(special)
        
        result += inverse
        return "".join(result)
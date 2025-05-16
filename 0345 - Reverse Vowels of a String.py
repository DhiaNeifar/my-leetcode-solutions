class Solution:
    def reverseVowels(self, s: str) -> str:
        right = 0
        left = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_list = [char for char in s]
        while right < left:
            if s_list[right] not in vowels:
                right += 1
            if s_list[left] not in vowels:
                left -= 1
            if s_list[right] in vowels and s_list[left] in vowels:
                s_list[right], s_list[left] = s_list[left], s_list[right]
                right += 1
                left -= 1
        return ''.join(s_list)
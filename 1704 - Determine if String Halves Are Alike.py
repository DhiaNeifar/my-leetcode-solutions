class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count_1, count_2 = 0, 0
        half = len(s) // 2
        vowels = ('a', 'e', 'i', 'o', 'u')
        for i in range(half):
            if s[i].lower() in vowels:
                count_1 += 1
            if s[i + half].lower() in vowels:
                count_2 += 1
        return count_1 == count_2
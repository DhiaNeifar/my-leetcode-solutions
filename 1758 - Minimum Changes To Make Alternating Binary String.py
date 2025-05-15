class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1:
            return 0

        l = []
        for i in range(len(s) // 2 + 1):
            l.append('0')
            l.append('1')
        count1, count2 = 0, 0

        for index in range(len(s)):
            if l[index] != s[index]:
                count1 += 1
            if l[len(l) - index - 1] != s[index]:
                count2 += 1
        return min(count1, count2)
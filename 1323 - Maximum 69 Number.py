class Solution:
    def maximum69Number (self, num: int) -> int:
        numlist = []
        while num:
            div, rest = divmod(num, 10)
            numlist.append(rest)
            num = div
        
        for i in range(len(numlist) - 1, -1, -1):
            if numlist[i] == 6:
                numlist[i] = 9
                break
        
        num = 0
        for i in range(len(numlist) - 1, -1, -1):
            num *= 10
            num += numlist[i]
        
        return num
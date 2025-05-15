class Solution:
    def trailingZeroes(self, n: int) -> int:
        # TOOK TOO LONG DIDNT WORK!!!!
        # if n <= 1:
            # return 0
        # else:
            # x = 1
            # for i in range (2, n + 1):
                # x *= i
            # a = 0
            # while not x % 10:
                # a += 1
                # x //= 10
            # return a
        if n < 5:
            return 0
        else:
            a2, a5 = 0, 0
            for i in range (2, n + 1):
                x2, x5 = i, i
                while not x2 % 2:
                    a2 += 1
                    x2 //= 2
                while not x5 % 5: 
                    a5 += 1
                    x5 //= 5
            return min(a2, a5)
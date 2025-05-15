class Solution:
    def climbStairs(self, n: int) -> int:
        if (n <= 1):
            return 1
        else:
            l = [1, 1]
            for i in range(n - 1):
                l.append(l[i] + l[i + 1])
            return(l[n])
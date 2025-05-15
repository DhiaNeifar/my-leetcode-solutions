class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [1]
        for i in range(n - 1):
            x_2, j = 1, 0
            while x_2 <= l[-1]:
                x_2 = l[j] * 2
                j += 1
            x_3, j = 1, 0
            while x_3 <= l[-1]:
                x_3 = l[j] * 3
                j += 1
            x_5, j = 1, 0
            while x_5 <= l[-1]:
                x_5 = l[j] * 5
                j += 1
            l.append(min(x_2, x_3, x_5))
        return l[-1]
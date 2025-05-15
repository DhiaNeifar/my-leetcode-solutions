class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr_index = -1
        maximum = ""
        for i in range(1, len(num) - 1):
            if num[i - 1] == num[i] == num[i + 1]:
                if num[i] > maximum:
                    maximum = num[i]
        return maximum * 3
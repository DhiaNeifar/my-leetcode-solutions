class Solution:
    def maxDiff(self, num: int) -> int:
        num_list = []
        while num:
            div, rest = divmod(num, 10)
            num_list.append(rest)
            num = div
        
        min_list = [digit for digit in num_list]

        golden = None
        for i in range(len(num_list) - 1, -1, -1):
            if num_list[i] != 9:
                golden = num_list[i]
                break

        if golden is not None:
            for i in range(len(num_list)):
                if num_list[i] == golden:
                    num_list[i] = 9
        
        golden = None
        ind = None
        change = 0

        for i in range(len(min_list) - 1, -1, -1):
            if min_list[i] != 1 and min_list[i] != 0:
                golden = min_list[i]
                ind = i
                break

        if golden is not None:
            if ind == len(min_list) - 1:
                change = 1
            
            for i in range(len(min_list)):
                if min_list[i] == golden:
                    min_list[i] = change

        result = 0
        for i in range(len(num_list) - 1, -1, -1):
            result *= 10
            result += num_list[i] - min_list[i]

        return result
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_list = []
        while num:
            div, rest = divmod(num, 10)
            num_list.append(rest)
            num = div
        
        golden = num_list[-1]
        min_list = [num if num != golden else 0 for num in num_list ]


        golden = None
        for i in range(len(num_list) - 1, -1, -1):
            if num_list[i] < 9:
                golden = num_list[i]
                break
        for i in range(len(num_list)):
            if num_list[i] == golden:
                num_list[i] = 9
        
        result = 0

        golden = num_list[-1]
        
        for i in range(len(num_list) - 1, -1, -1):
            diff = min_list[i]

            result *= 10
            result += num_list[i] - diff
        
        return result
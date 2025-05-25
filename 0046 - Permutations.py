class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        solution = []

        def backtracking(status):
            if len(solution) == len(nums):
                result.append(solution.copy())
                return

            for index, stat in enumerate(status):
                if not stat:
                    solution.append(nums[index])
                    status[index] = True
                    backtracking(status)
                    status[index] = False
                    solution.pop()
        
        backtracking([False for _ in nums])
        return result
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        solution = []

        def backtracking(curr_index, curr_sum):
            if curr_sum == target:
                result.append(solution.copy())
                return
            
            i = curr_index
            while i < len(candidates) and curr_sum < target:
                solution.append(candidates[i])
                backtracking(i, curr_sum + candidates[i])
                solution.pop()
                i += 1
        backtracking(0, 0)
        return result
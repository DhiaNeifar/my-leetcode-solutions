class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]

        stack = []
        for curr_day, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                prev_day = stack.pop()
                result[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        return result
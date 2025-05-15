class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_ = set()
        curr_max = nums[0]
        for num in nums:
            curr_max = max(curr_max, num)
            set_.add(num)
            if len(set_) >= 3:
                break
        if len(set_) < 3:
            return curr_max
        curr_max = max(nums)
        i = 0
        while i < len(nums) and nums[i] == curr_max:
            i += 1
        second_max = nums[i]
        j = i + 1
        while j < len(nums) and (nums[j] == second_max or nums[j] == curr_max):
            j += 1
        third_max = nums[j]
        if second_max < third_max:
            second_max, third_max = third_max, second_max 
        for num in nums:
            if second_max < num < curr_max:
                second_max = num
        for num in nums:
            if third_max < num < second_max:
                third_max = num
        return third_max
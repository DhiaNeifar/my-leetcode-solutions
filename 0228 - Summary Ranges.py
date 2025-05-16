class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        
        if len(nums) == 1:
            return [str(nums[0])]
        
        result = []
        start = nums[0]
        range_ = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == range_ + 1:
                range_ += 1
            else:
                if range_ == start:
                    result.append(str(range_))
                else:
                    result.append(f"{start}->{range_}")
                start = nums[i]
                range_ = nums[i]
        if range_ == start:
            result.append(str(range_))
        else:
            result.append(f"{start}->{range_}")
        return result
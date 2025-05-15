class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if len(nums) == 1:
            return nums
        inverse_list(nums, 0, len(nums) - 1)

        inverse_list(nums, 0, k - 1)
        inverse_list(nums, k, len(nums) - 1)

def inverse_list(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
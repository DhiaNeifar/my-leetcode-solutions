class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
                return -1

        pivot = find_pivot(nums)
        n = len(nums)

        # Decide which subarray to search
        if nums[pivot] <= target <= nums[-1]:
            # Search in the right part
            return binary_search(pivot, n - 1, nums, target)
        else:
            # Search in the left part
            return binary_search(0, pivot - 1, nums, target)
    
def binary_search(start, end, arr, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def find_pivot(nums):
    # Returns the index of the smallest value (the pivot)
    left, right = 0, len(nums) - 1
    if nums[left] < nums[right]:  # Not rotated
        return 0
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            result = binary_search(numbers, i + 1, len(numbers) - 1, target - numbers[i])
            if result:
                return [i + 1, result + 1] 
def binary_search(table, begin, end, val):
    while begin <= end:
        mid = (begin + end) // 2
        if table[mid] == val:
            return mid
        if table[mid] < val:
            begin = mid + 1
        if table[mid] > val:
            end = mid - 1
    return 0
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = 0
        for num in arr:
            if num == 0:
                zeros += 1

        i = len(arr) - 1
        while i > -1:
            if i + zeros < len(arr):
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < len(arr):
                    arr[i + zeros] = 0
            i -= 1
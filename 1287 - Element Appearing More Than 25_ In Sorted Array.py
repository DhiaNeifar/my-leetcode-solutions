class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return arr[0]
        lim = len(arr) / 4
        element, count = arr[0], 1
        for next_element in arr[1:]:
            if next_element == element:
                count += 1
            else:
                element = next_element
                count = 1
            if count > lim:
                return element
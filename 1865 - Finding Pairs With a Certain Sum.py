class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = {}
        for num in nums1:
            self.nums1[num] = self.nums1.get(num, 0) + 1
        self.nums2 = {}
        for num in nums2:
            self.nums2[num] = self.nums2.get(num, 0) + 1
        self.nums2_ = nums2

    def add(self, index: int, val: int) -> None:
        original_number = self.nums2_[index]
        new_number = original_number + val
        self.nums2[new_number] = self.nums2.get(new_number, 0) + 1
        self.nums2[original_number] -= 1
        self.nums2_[index] += val
        if self.nums2[original_number] == 0:
            del self.nums2[original_number]

    def count(self, tot: int) -> int:
        result = 0
        for num in self.nums2:
            difference = tot - num
            if difference in self.nums1:
                result += self.nums2[num] * self.nums1[difference]
        return result


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
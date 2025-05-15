class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        XORList = [0]
        total_sum = 0
        for num in nums:
            XORListLength = len(XORList)
            for i in range(XORListLength):
                xor_result = XORList[i] ^ num
                total_sum += xor_result
                XORList.append(xor_result)
        return total_sum
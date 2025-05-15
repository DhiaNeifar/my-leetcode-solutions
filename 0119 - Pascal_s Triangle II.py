class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = [1 for _ in range(rowIndex + 1)]
        if rowIndex == 0:
            return l
        l[1], l[-2] = rowIndex, rowIndex
        for i in range(2, rowIndex // 2 + 1):
            l[i] = l[i - 1] * (rowIndex - (i - 1)) // i
            l[rowIndex - i] = l[i]
        return l
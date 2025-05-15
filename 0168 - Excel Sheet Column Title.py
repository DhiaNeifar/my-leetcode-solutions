class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = []
        while columnNumber:
            columnNumber -= 1
            digit = columnNumber % 26
            output.append(chr(digit + 65))
            columnNumber = (columnNumber - digit) // 26
        result = ''.join(output[::-1])
        return result
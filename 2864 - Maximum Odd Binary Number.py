class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_ones = 0
        bits = []
        for bit in s:
            if bit == '1':
                num_ones += 1
        for i in range(num_ones - 1):
            bits.append('1')
        for i in range(len(s) - num_ones):
            bits.append('0')
        bits.append('1')
        return ''.join(bits)
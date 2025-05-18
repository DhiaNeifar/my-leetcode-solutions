class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        while n:
            bits.append(n % 2)
            n //= 2
        
        while len(bits) < 32:
            bits.append(0)
        
        result = 0
        power_two = 1
        for i in range(len(bits) - 1, -1, -1):
            bit = bits[i]
            if bit:
                result += power_two
            power_two *= 2
        return result
class Solution:
    def countBits(self, n: int) -> List[int]:
        table = [0]
        result = [0]
        for i in range(n):
            if table[0] == 0:
                table[0] = 1
            else:
                table[0] = 0
                j = 1
                while j < len(table) and table[j] == 1:
                    table[j] = 0
                    j += 1
                if j == len(table):
                    table.append(1)
                else:
                    table[j] = 1
            result.append(sum(table))
        return result